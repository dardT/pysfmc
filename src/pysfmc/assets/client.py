"""Main Assets client for SFMC Assets (Content Builder) API."""

from typing import TYPE_CHECKING, Optional

from .categories import AsyncCategoriesClient, CategoriesClient

if TYPE_CHECKING:
    from ..client import AsyncSFMCClient, SFMCClient


class AssetsClient:
    """Synchronous client for SFMC Assets (Content Builder) API."""

    def __init__(self, client: "SFMCClient"):
        self._client = client
        self._categories: Optional[CategoriesClient] = None

    @property
    def categories(self) -> CategoriesClient:
        """Access to categories (folders) operations."""
        if self._categories is None:
            self._categories = CategoriesClient(self._client)
        return self._categories


class AsyncAssetsClient:
    """Asynchronous client for SFMC Assets (Content Builder) API."""

    def __init__(self, client: "AsyncSFMCClient"):
        self._client = client
        self._categories: Optional[AsyncCategoriesClient] = None

    @property
    def categories(self) -> AsyncCategoriesClient:
        """Access to categories (folders) operations."""
        if self._categories is None:
            self._categories = AsyncCategoriesClient(self._client)
        return self._categories
