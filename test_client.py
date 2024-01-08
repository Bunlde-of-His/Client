"""Module for testing email verification and domain search services.

This module contains a test client that demonstrates the use of the
EmailVerifierService and DomainSearchService classes for verifying email
addresses and searching for information about domains.
"""
import logging
from typing import Optional

from email_verifier import EmailVerifier, DomainSearch
from service import VerificationResultManager

logging.basicConfig(level=logging.INFO)


class EmailVerifierService(object):
    """Service for verifying and storing email verification results."""

    def __init__(self, email_verifier_client: EmailVerifier) -> None:
        """Initialize the EmailVerifierService instance."""
        self.email_verifier_client: EmailVerifier = email_verifier_client
        self.result_manager = VerificationResultManager()

    def verify_and_store_email(self, email: str) -> bool:
        """Verify the provided email and store the result."""
        verification_result: Optional[dict] = self.email_verifier_client.verify_email(email)
        if verification_result:
            self.result_manager.create_result(verification_result)
            return True
        return False

    def get_results_manager(self) -> VerificationResultManager:
        """Get the manager for verification results."""
        return self.result_manager


class DomainSearchService(object):
    """Service for searching and storing domain information."""

    def __init__(self, domain_search_client: DomainSearch) -> None:
        """Initialize the DomainSearchService instance."""
        self.domain_search_client: DomainSearch = domain_search_client
        self.result_manager = VerificationResultManager()

    def search_and_store_domain(self, domain: str) -> bool:
        """Search information about the provided domain and store the result."""
        domain_search_result: Optional[dict] = self.domain_search_client.search_domain(domain)
        if domain_search_result:
            self.result_manager.create_result(domain_search_result)
            return True
        return False

    def get_results_manager(self) -> VerificationResultManager:
        """Get the manager for search results."""
        return self.result_manager


if __name__ == '__main__':

    api_key_example = '9ad67b74ed2d3fb60d5cb68ee7a209098c8ae601'
    verifier_client = EmailVerifier(api_key_example)
    verifier_service = EmailVerifierService(verifier_client)

    email_to_verify_example = 'zhoritihon@gmail.com'
    if verifier_service.verify_and_store_email(email_to_verify_example):
        logging.info('\nEmail Verification successful.')
        verifier_service_results = (verifier_service.get_results_manager().read_results())
        logging.info('All Email Verification Results: {result}'.format(result=verifier_service_results))
    else:
        logging.error('Email Verification failed.')

    domain_search_client_example = DomainSearch(api_key_example)
    domain_service = DomainSearchService(domain_search_client_example)

    domain_to_search_example = 'https://git-scm.com/'
    if domain_service.search_and_store_domain(domain_to_search_example):
        logging.info('\nDomain Search successful.')
        domain_search_results = (domain_service.get_results_manager().read_results())
        logging.info('All Domain Search Results: {result}'.format(result=domain_search_results))
    else:
        logging.error('\nDomain Search failed.')
