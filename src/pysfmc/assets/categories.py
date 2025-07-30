"""Categories client for SFMC Assets (Content Builder) API."""

from typing import TYPE_CHECKING, Optional

from ..models.assets import Category, CategoryCreate, CategoryResponse

if TYPE_CHECKING:
    from ..client import AsyncSFMCClient, SFMCClient


class CategoriesClient:
    """Synchronous client for Content Builder category operations."""

    def __init__(self, client: "SFMCClient"):
        self._client = client

    def get_categories(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[str] = None,
        filter_expr: Optional[str] = None,
        scope: Optional[str] = None,
        parent_id: Optional[int] = None,
    ) -> CategoryResponse:
        """Get categories with optional filtering and pagination.

        Args:
            page: Page number (1-based)
            page_size: Number of items per page (1-50)
            order_by: Sort order (e.g., 'name asc', 'name desc')
            filter_expr: Filter expression (only 'parentId eq <value>' is supported by SFMC API)
            scope: Scope filter (e.g., 'Shared')
            parent_id: Filter by parent category ID

        Returns:
            CategoryResponse with paginated results
        """
        params = {}

        if page is not None:
            params["$page"] = page
        if page_size is not None:
            params["$pageSize"] = page_size
        if order_by is not None:
            params["$orderBy"] = order_by
        if filter_expr is not None:
            params["$filter"] = filter_expr
        if scope is not None:
            params["scope"] = scope
        if parent_id is not None:
            # Add parent_id to filter expression
            parent_filter = f"parentId eq {parent_id}"
            if filter_expr:
                params["$filter"] = f"({filter_expr}) and ({parent_filter})"
            else:
                params["$filter"] = parent_filter

        response_data = self._client.get("/asset/v1/content/categories", params=params)
        return CategoryResponse(**response_data)

    def get_category_by_id(self, category_id: int) -> Category:
        """Get a specific category by ID.

        Args:
            category_id: The category ID to retrieve

        Returns:
            Category model instance
        """
        response_data = self._client.get(f"/asset/v1/content/categories/{category_id}")
        return Category(**response_data)

    def create_category(
        self,
        name: str,
        parent_id: int,
    ) -> Category:
        """Create a new category.

        Args:
            name: Category name
            parent_id: Parent category ID

        Returns:
            Created Category model instance
        """
        category_data = CategoryCreate(name=name, parent_id=parent_id)

        response_data = self._client.post(
            "/asset/v1/content/categories", json=category_data
        )
        return Category(**response_data)


class AsyncCategoriesClient:
    """Asynchronous client for Content Builder category operations."""

    def __init__(self, client: "AsyncSFMCClient"):
        self._client = client

    async def get_categories(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[str] = None,
        filter_expr: Optional[str] = None,
        scope: Optional[str] = None,
        parent_id: Optional[int] = None,
    ) -> CategoryResponse:
        """Get categories with optional filtering and pagination.

        Args:
            page: Page number (1-based)
            page_size: Number of items per page (1-50)
            order_by: Sort order (e.g., 'name asc', 'name desc')
            filter_expr: Filter expression (only 'parentId eq <value>' is supported by SFMC API)
            scope: Scope filter (e.g., 'Shared')
            parent_id: Filter by parent category ID

        Returns:
            CategoryResponse with paginated results
        """
        params = {}

        if page is not None:
            params["$page"] = page
        if page_size is not None:
            params["$pageSize"] = page_size
        if order_by is not None:
            params["$orderBy"] = order_by
        if filter_expr is not None:
            params["$filter"] = filter_expr
        if scope is not None:
            params["scope"] = scope
        if parent_id is not None:
            # Add parent_id to filter expression
            parent_filter = f"parentId eq {parent_id}"
            if filter_expr:
                params["$filter"] = f"({filter_expr}) and ({parent_filter})"
            else:
                params["$filter"] = parent_filter

        response_data = await self._client.get(
            "/asset/v1/content/categories", params=params
        )
        return CategoryResponse(**response_data)

    async def get_category_by_id(self, category_id: int) -> Category:
        """Get a specific category by ID.

        Args:
            category_id: The category ID to retrieve

        Returns:
            Category model instance
        """
        response_data = await self._client.get(
            f"/asset/v1/content/categories/{category_id}"
        )
        return Category(**response_data)

    async def create_category(
        self,
        name: str,
        parent_id: int,
    ) -> Category:
        """Create a new category.

        Args:
            name: Category name
            parent_id: Parent category ID

        Returns:
            Created Category model instance
        """
        category_data = CategoryCreate(
            name=name,
            parent_id=parent_id,
        )

        response_data = await self._client.post(
            "/asset/v1/content/categories", json=category_data
        )
        return Category(**response_data)
