"""Asset models for SFMC Assets (Content Builder) API."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..base import SFMC_MODEL_CONFIG
from .categories import Category


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
    user_id: Optional[str] = Field(None, alias="userId", description="User ID as string")
    email: Optional[str] = Field(None, description="User email")
    name: Optional[str] = Field(None, description="User name")


class Status(BaseModel):
    """Model for SFMC asset status information."""

    model_config = SFMC_MODEL_CONFIG

    id: Optional[int] = Field(None, description="Status ID")
    name: Optional[str] = Field(None, description="Status name")


class ThumbNail(BaseModel):
    model_config = SFMC_MODEL_CONFIG

    thumbnail_url: Optional[str] = Field(
        None, alias="thumbnailUrl", description="Asset thumbnail URL"
    )


class Asset(BaseModel):
    """Model for SFMC Content Builder asset.

    Based on official SFMC Asset API specification.
    All fields are optional to handle different asset response formats.
    """

    model_config = SFMC_MODEL_CONFIG

    # Core identifiers (read-only, searchable)
    id: Optional[int] = Field(None, description="Asset ID (read-only, searchable)")
    customer_key: Optional[str] = Field(
        None, alias="customerKey", description="Customer key reference (searchable)"
    )
    object_id: Optional[str] = Field(None, alias="objectID", description="Object ID (searchable)")

    # Asset metadata
    name: Optional[str] = Field(None, description="Asset name (required for creation)")
    description: Optional[str] = Field(None, description="Asset description")
    content_type: Optional[str] = Field(
        None, alias="contentType", description="Content type"
    )
    asset_type: Optional[AssetType] = Field(
        None, alias="assetType", description="Asset type information"
    )
    available_views: Optional[List[str]] = Field(
        None, alias="availableViews", description="Available views for the asset"
    )
    legacy_data: Optional[Dict[str, Any]] = Field(
        None, alias="legacyData", description="Legacy data information"
    )
    model_version: Optional[int] = Field(
        None, alias="modelVersion", description="Model version"
    )
    
    # Content and design fields
    content: Optional[str] = Field(None, description="Asset content")
    design: Optional[str] = Field(None, description="Asset design")
    super_content: Optional[str] = Field(
        None, alias="superContent", description="Asset super content"
    )
    generate_from: Optional[str] = Field(
        None, alias="generateFrom", description="Generate from reference"
    )
    
    # Data and metadata
    data: Optional[Dict[str, Any]] = Field(None, description="Asset data object")
    meta: Optional[Dict[str, Any]] = Field(None, description="Asset metadata")
    custom_fields: Optional[Dict[str, Any]] = Field(
        None, alias="customFields", description="Custom field data"
    )
    
    # Template and structure fields
    views: Optional[Dict[str, Any]] = Field(
        None, description="Asset views (email template slots, etc.)"
    )
    slots: Optional[Dict[str, Any]] = Field(None, description="Asset slots")
    blocks: Optional[Dict[str, Any]] = Field(None, description="Asset blocks")
    template: Optional[Dict[str, Any]] = Field(None, description="Template information")
    min_blocks: Optional[int] = Field(
        None, alias="minBlocks", description="Minimum number of blocks"
    )
    max_blocks: Optional[int] = Field(
        None, alias="maxBlocks", description="Maximum number of blocks"
    )
    
    # Version and status
    version: Optional[int] = Field(None, description="Asset version number (read-only, searchable)")
    locked: Optional[bool] = Field(None, description="Whether asset is locked")
    status: Optional[Status] = Field(None, description="Asset status information")
    
    # Date fields
    active_date: Optional[str] = Field(
        None, alias="activeDate", description="Asset active date"
    )
    expiration_date: Optional[str] = Field(
        None, alias="expirationDate", description="Asset expiration date"
    )
    created_date: Optional[str] = Field(
        None, alias="createdDate", description="Creation date (read-only, searchable)"
    )
    modified_date: Optional[str] = Field(
        None, alias="modifiedDate", description="Last modified date (read-only, searchable)"
    )
    
    # Organization and categorization
    category: Optional[Category] = Field(None, description="Asset category information")
    tags: Optional[List[str]] = Field(None, description="Asset tags")
    channels: Optional[Dict[str, Any]] = Field(None, description="Channel information")
    
    # Ownership (read-only, searchable)
    owner: Optional[Owner] = Field(None, description="Asset owner information (read-only, searchable)")
    created_by: Optional[Owner] = Field(
        None, alias="createdBy", description="Created by user information (read-only, searchable)"
    )
    modified_by: Optional[Owner] = Field(
        None, alias="modifiedBy", description="Last modified by user information (read-only, searchable)"
    )
    
    # Enterprise and member info (read-only, searchable)
    enterprise_id: Optional[int] = Field(
        None, alias="enterpriseId", description="Enterprise ID (read-only, searchable)"
    )
    member_id: Optional[int] = Field(
        None, alias="memberId", description="Member ID (read-only, searchable)"
    )
    
    # File and media properties
    file: Optional[Dict[str, Any]] = Field(None, description="File information")
    thumbnail: Optional[ThumbNail] = Field(
        None, description="Asset thumbnail information"
    )
    
    # Business unit and availability
    business_unit_availability: Optional[Dict[str, Any]] = Field(
        None, alias="businessUnitAvailability", description="Business unit availability settings"
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
