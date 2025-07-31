"""Content client for SFMC Assets (Content Builder) API."""

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from ..models.assets import Asset, AssetType

if TYPE_CHECKING:
    from ..client import AsyncSFMCClient, SFMCClient


class ContentClient:
    """Synchronous client for Content Builder asset content operations."""

    def __init__(self, client: "SFMCClient"):
        self._client = client

    def create_asset(
        self,
        name: str,
        content_type: str,
        asset_type_id: int,
        customer_key: str,
        description: Optional[str] = None,
        content: Optional[str] = None,
        design: Optional[str] = None,
        super_content: Optional[str] = None,
        tags: Optional[List[str]] = None,
        category_id: Optional[int] = None,
        data: Optional[Dict[str, Any]] = None,
        meta: Optional[Dict[str, Any]] = None,
        custom_fields: Optional[Dict[str, Any]] = None,
        views: Optional[Dict[str, Any]] = None,
        slots: Optional[Dict[str, Any]] = None,
        blocks: Optional[Dict[str, Any]] = None,
        template: Optional[Dict[str, Any]] = None,
        file_properties: Optional[Dict[str, Any]] = None,
    ) -> Asset:
        """Create a new asset in Content Builder.

        Args:
            name: Asset name (required, max 200 characters)
            content_type: Type of content attribute (required)
            asset_type_id: Asset type ID (required)
            customer_key: Reference to customer's private ID/name (required)
            description: Asset description
            content: Asset content
            design: Asset design
            super_content: Asset super content
            tags: List of asset tags
            category_id: Category ID for the asset
            data: Asset data object
            meta: Asset metadata
            custom_fields: Custom field data
            views: Asset views (email template slots, etc.)
            slots: Asset slots
            blocks: Asset blocks
            template: Template information
            file_properties: File properties for file-based assets

        Returns:
            Asset model instance of the created asset

        Raises:
            SFMCValidationError: If required fields are missing
            SFMCPermissionError: If insufficient permissions
            SFMCAPIError: For other API errors
        """
        # Create Asset object directly from parameters
        asset = Asset(
            name=name,
            content_type=content_type,
            customer_key=customer_key,
            asset_type=AssetType(id=asset_type_id),
            description=description,
            content=content,
            design=design,
            super_content=super_content,
            tags=tags,
            category={"id": category_id} if category_id is not None else None,
            data=data,
            meta=meta,
            custom_fields=custom_fields,
            views=views,
            slots=slots,
            blocks=blocks,
            template=template,
            file=file_properties,
        )

        # Make the API call with the Asset model (will be serialized automatically)
        response_data = self._client.post("/asset/v1/content/assets", json=asset)
        return Asset(**response_data)


class AsyncContentClient:
    """Asynchronous client for Content Builder asset content operations."""

    def __init__(self, client: "AsyncSFMCClient"):
        self._client = client

    async def create_asset(
        self,
        name: str,
        content_type: str,
        asset_type_id: int,
        customer_key: str,
        description: Optional[str] = None,
        content: Optional[str] = None,
        design: Optional[str] = None,
        super_content: Optional[str] = None,
        tags: Optional[List[str]] = None,
        category_id: Optional[int] = None,
        data: Optional[Dict[str, Any]] = None,
        meta: Optional[Dict[str, Any]] = None,
        custom_fields: Optional[Dict[str, Any]] = None,
        views: Optional[Dict[str, Any]] = None,
        slots: Optional[Dict[str, Any]] = None,
        blocks: Optional[Dict[str, Any]] = None,
        template: Optional[Dict[str, Any]] = None,
        file_properties: Optional[Dict[str, Any]] = None,
    ) -> Asset:
        """Create a new asset in Content Builder.

        Args:
            name: Asset name (required, max 200 characters)
            content_type: Type of content attribute (required)
            asset_type_id: Asset type ID (required)
            customer_key: Reference to customer's private ID/name (required)
            description: Asset description
            content: Asset content
            design: Asset design
            super_content: Asset super content
            tags: List of asset tags
            category_id: Category ID for the asset
            data: Asset data object
            meta: Asset metadata
            custom_fields: Custom field data
            views: Asset views (email template slots, etc.)
            slots: Asset slots
            blocks: Asset blocks
            template: Template information
            file_properties: File properties for file-based assets

        Returns:
            Asset model instance of the created asset

        Raises:
            SFMCValidationError: If required fields are missing
            SFMCPermissionError: If insufficient permissions
            SFMCAPIError: For other API errors
        """
        # Create Asset object directly from parameters
        asset = Asset(
            name=name,
            content_type=content_type,
            customer_key=customer_key,
            asset_type=AssetType(id=asset_type_id),
            description=description,
            content=content,
            design=design,
            super_content=super_content,
            tags=tags,
            category={"id": category_id} if category_id is not None else None,
            data=data,
            meta=meta,
            custom_fields=custom_fields,
            views=views,
            slots=slots,
            blocks=blocks,
            template=template,
            file=file_properties,
        )

        # Make the API call with the Asset model (will be serialized automatically)
        response_data = await self._client.post("/asset/v1/content/assets", json=asset)
        return Asset(**response_data)