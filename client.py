"""Module for interacting with the Hunter.io API."""
from typing import Any, Dict, Optional

import requests


class Client(object):
    """Class for interacting with the Hunter.io API."""

    def __init__(self, api_key: str) -> None:
        """Initialize the Client instance."""
        self.api_key: str = api_key
        self.base_url: str = 'https://api.hunter.io/v2/'

    def request_api(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a request to the Hunter.io API."""
        if params is None:
            params = {}
        params['api_key'] = self.api_key
        response = requests.get(self.base_url + endpoint, params=params, timeout=10)
        return response.json()

    def verify_email(self, email: str) -> Dict[str, Any]:
        """Verify the provided email using the Hunter.io API."""
        endpoint: str = 'email-verifier'
        email_params: Dict[str, str] = {'email': email}
        return self.request_api(endpoint, params=email_params)

    def domain_search(self, domain: str) -> Dict[str, Any]:
        """Search information about a domain using the Hunter.io API."""
        endpoint: str = 'domain-search'
        domain_params: Dict[str, str] = {'domain': domain}
        return self.request_api(endpoint, params=domain_params)
