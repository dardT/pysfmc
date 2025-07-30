"""Python client for Salesforce Marketing Cloud (SFMC) API."""

from .assets import AssetsClient, AsyncAssetsClient
from .auth import SFMCSettings
from .client import AsyncSFMCClient, SFMCClient
from .config import SFMCConfig
from .exceptions import (SFMCAuthenticationError, SFMCAuthorizationError,
                         SFMCConnectionError, SFMCError, SFMCNotFoundError,
                         SFMCRateLimitError, SFMCServerError,
                         SFMCValidationError)
from .models.assets import Category, CategoryCreate, CategoryResponse

__version__ = "0.1.0"

__all__ = [
    # Main classes
    "SFMCClient",
    "AsyncSFMCClient",
    "SFMCSettings",
    "SFMCConfig",
    # Assets clients
    "AssetsClient",
    "AsyncAssetsClient",
    # Models
    "Category",
    "CategoryCreate",
    "CategoryResponse",
    # Exceptions
    "SFMCError",
    "SFMCAuthenticationError",
    "SFMCAuthorizationError",
    "SFMCValidationError",
    "SFMCNotFoundError",
    "SFMCRateLimitError",
    "SFMCServerError",
    "SFMCConnectionError",
]
