"""Assets models for SFMC API."""

from .assets import (
    Asset,
    AssetFilter,
    AssetResponse,
    AssetType,
    AssetTypeCreate,
    CreateAsset,
    Owner,
    Status,
)
from .block_types import (
    create_block_by_name,
    create_block_by_type,
)
from .blocks import (
    Block,
    Slot,
)
from .categories import Category, CategoryCreate, CategoryFilter, CategoryResponse
from .create_models import (
    CreateHtmlEmail,
    CreateTemplateBasedEmail,
    create_email_views,
    create_simple_slot,
)
from .views import (
    Channels,
    EmailViews,
    HtmlView,
    PreheaderView,
    SubjectLineView,
    TemplateReference,
    TextView,
)

__all__ = [
    # Category models
    "Category",
    "CategoryCreate",
    "CategoryResponse",
    "CategoryFilter",
    # Asset models
    "Asset",
    "AssetResponse",
    "AssetFilter",
    "AssetType",
    "AssetTypeCreate",
    "CreateAsset",
    "Owner",
    "Status",
    # Block and slot models
    "Block",
    "Slot",
    "BlockAssetType",
    "BlockMeta",
    "WrapperStyles",
    "EmailData",
    "EmailOptions",
    # Specialized block types
    "TextBlock",
    "ImageBlock",
    "ButtonBlock",
    "SocialFollowBlock",
    "LayoutBlock",
    "create_block_by_type",
    "create_block_by_name",
    # View models
    "EmailViews",
    "HtmlView",
    "TextView",
    "SubjectLineView",
    "PreheaderView",
    "TemplateReference",
    "Channels",
    # Enhanced create models
    "CreateTemplateBasedEmail",
    "CreateHtmlEmail",
    "create_simple_slot",
    "create_email_views",
]
