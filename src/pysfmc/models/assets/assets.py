"""Asset models for SFMC Assets (Content Builder) API."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..base import SFMC_MODEL_CONFIG


class AssetType(BaseModel):
    """Model for SFMC Asset Type information."""

    model_config = SFMC_MODEL_CONFIG

    id: Optional[int] = Field(None, description="Asset type ID")
    name: Optional[str] = Field(None, description="Asset type name")
    display_name: Optional[str] = Field(
        None, alias="displayName", description="Asset type display name"
    )


class Owner(BaseModel):
    """Model for SFMC asset owner/user information."""

    model_config = SFMC_MODEL_CONFIG

    id: Optional[int] = Field(None, description="User ID")
    email: Optional[str] = Field(None, description="User email")
    name: Optional[str] = Field(None, description="User name")


class Status(BaseModel):
    """Model for SFMC asset status information."""

    model_config = SFMC_MODEL_CONFIG

    id: Optional[int] = Field(None, description="Status ID")
    name: Optional[str] = Field(None, description="Status name")


class Category(BaseModel):
    """Model for SFMC asset category information."""

    model_config = SFMC_MODEL_CONFIG

    id: Optional[int] = Field(None, description="Category ID")
    parent_id: Optional[int] = Field(
        None, alias="parentId", description="Parent category ID"
    )
    name: Optional[str] = Field(None, description="Category name")


class Asset(BaseModel):
    """Model for SFMC Content Builder asset.

    Uses flexible schema to accommodate the varying structure of different asset types.
    All fields are optional to handle different asset response formats.
    """

    model_config = SFMC_MODEL_CONFIG

    # Core identifiers
    id: Optional[int] = Field(None, description="Asset ID")
    customer_key: Optional[str] = Field(
        None, alias="customerKey", description="Customer key reference"
    )
    object_id: Optional[str] = Field(None, alias="objectID", description="Object ID")

    # Asset metadata
    content_type: Optional[str] = Field(
        None, alias="contentType", description="Content type"
    )
    asset_type: Optional[AssetType] = Field(
        None, alias="assetType", description="Asset type information"
    )
    name: Optional[str] = Field(None, description="Asset name")
    description: Optional[str] = Field(None, description="Asset description")

    # Content fields
    content: Optional[str] = Field(None, description="Asset content")
    design: Optional[str] = Field(None, description="Asset design")
    super_content: Optional[str] = Field(
        None, alias="superContent", description="Asset super content"
    )
    data: Optional[Dict[str, Any]] = Field(None, description="Asset data object")
    views: Optional[Dict[str, Any]] = Field(
        None, description="Asset views (email template slots, etc.)"
    )

    # Version and status
    version: Optional[int] = Field(None, description="Asset version number")
    model_version: Optional[int] = Field(
        None, alias="modelVersion", description="Model version"
    )
    locked: Optional[bool] = Field(None, description="Whether asset is locked")
    status: Optional[Status] = Field(None, description="Asset status information")

    # Organization
    category: Optional[Category] = Field(None, description="Asset category information")
    tags: Optional[List[str]] = Field(default_factory=list, description="Asset tags")

    # Ownership and dates
    owner: Optional[Owner] = Field(None, description="Asset owner information")
    created_date: Optional[str] = Field(
        None, alias="createdDate", description="Creation date"
    )
    created_by: Optional[Owner] = Field(
        None, alias="createdBy", description="Created by user information"
    )
    modified_date: Optional[str] = Field(
        None, alias="modifiedDate", description="Last modified date"
    )
    modified_by: Optional[Owner] = Field(
        None, alias="modifiedBy", description="Last modified by user information"
    )

    # Enterprise info
    enterprise_id: Optional[int] = Field(
        None, alias="enterpriseId", description="Enterprise ID"
    )
    member_id: Optional[int] = Field(None, alias="memberId", description="Member ID")

    # Sharing and media
    sharing_properties: Optional[Dict[str, Any]] = Field(
        None, alias="sharingProperties", description="Sharing configuration"
    )
    thumbnail: Optional[Dict[str, Any]] = Field(
        None, description="Asset thumbnail information"
    )
    thumbnail_url: Optional[str] = Field(
        None, alias="thumbnailUrl", description="Asset thumbnail URL"
    )
    file_properties: Optional[Dict[str, Any]] = Field(
        None, alias="fileProperties", description="File properties"
    )


class AssetResponse(BaseModel):
    """Model for paginated asset response."""

    model_config = SFMC_MODEL_CONFIG

    count: int = Field(..., description="Total number of assets")
    page: int = Field(..., description="Current page number")
    page_size: int = Field(
        ..., alias="pageSize", description="Number of items per page"
    )
    items: List[Asset] = Field(default_factory=list, description="List of assets")
    links: Optional[Dict[str, Any]] = Field(
        default_factory=dict, description="Pagination links"
    )


class AssetFilter(BaseModel):
    """Model for asset filtering parameters."""

    model_config = SFMC_MODEL_CONFIG

    page: Optional[int] = Field(None, alias="$page", description="Page number", ge=1)
    page_size: Optional[int] = Field(
        None, alias="$pageSize", description="Items per page", ge=1, le=50
    )
    order_by: Optional[str] = Field(
        None, alias="$orderBy", description="Sort order (e.g., 'Name desc')"
    )
    filter: Optional[str] = Field(
        None,
        alias="$filter",
        description="Filter expression (supports eq, neq, lt, lte, gt, gte, like operators)",
    )
    fields: Optional[str] = Field(
        None, alias="$fields", description="Comma-separated list of fields to return"
    )
