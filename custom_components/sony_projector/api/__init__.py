"""
API package for sony_projector.

Architecture:
    Three-layer data flow: Entities → Coordinator → API Client.
    Only the coordinator should call the API client. Entities must never
    import or call the API client directly.

Exception hierarchy:
    SonySDCPApiClientError (base)
    ├── SonySDCPApiClientCommunicationError (network/timeout)
    └── SonySDCPApiClientAuthenticationError (401/403)

Coordinator exception mapping:
    ApiClientAuthenticationError → ConfigEntryAuthFailed (triggers reauth)
    ApiClientCommunicationError → UpdateFailed (auto-retry)
    ApiClientError             → UpdateFailed (auto-retry)
"""

from .client import (
    SonySDCPApiClient,
    SonySDCPApiClientAuthenticationError,
    SonySDCPApiClientCommunicationError,
    SonySDCPApiClientError,
)

__all__ = [
    "SonySDCPApiClient",
    "SonySDCPApiClientAuthenticationError",
    "SonySDCPApiClientCommunicationError",
    "SonySDCPApiClientError",
]
