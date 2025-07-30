"""Assets clients for SFMC API."""

from .categories import AsyncCategoriesClient, CategoriesClient
from .client import AssetsClient, AsyncAssetsClient

__all__ = [
    "AssetsClient",
    "AsyncAssetsClient",
    "CategoriesClient",
    "AsyncCategoriesClient",
]
