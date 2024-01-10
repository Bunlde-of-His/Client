"""Module for managing and storing verification results."""
from typing import Any, Dict, Optional


class ResultService(object):
    """Class for managing and storing verification results."""

    def __init__(self) -> None:
        """Initialize the ResultService instance."""
        self.email_results: Dict[str, Any] = {}
        self.domain_results: Dict[str, Any] = {}

    def add_email_result(self, email: str, verification_result: Any) -> None:
        """Add email verification result to the service."""
        self.email_results[email] = verification_result

    def get_email_result(self, email: str) -> Optional[Any]:
        """Get email verification result from the service."""
        return self.email_results.get(email)

    def delete_email_result(self, email: str) -> None:
        """Delete email verification result from the service."""
        self.email_results.pop(email, None)

    def add_domain_result(self, domain: str, search_result: Any) -> None:
        """Add domain search result to the service."""
        self.domain_results[domain] = search_result

    def get_domain_result(self, domain: str) -> Optional[Any]:
        """Get domain search result from the service."""
        return self.domain_results.get(domain)

    def delete_domain_result(self, domain: str) -> None:
        """Delete domain search result from the service."""
        self.domain_results.pop(domain, None)
