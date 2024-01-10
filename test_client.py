"""Module with a simple test for the Hunter.io API client and result service."""
import logging
from typing import Optional, Dict, Any

from client import Client
from result_service import ResultService

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    hunter_api_key: str = '9ad67b74ed2d3fb60d5cb68ee7a209098c8ae601'
    email_to_verify: str = 'zhoritihon@gmail.com'
    domain_to_search: str = 'https://git-scm.com/'

    client: Client = Client(api_key=hunter_api_key)

    result_service: ResultService = ResultService()

    email_verification_result: Optional[Dict[str, Any]] = client.verify_email(email_to_verify)

    result_service.add_email_result(email_to_verify, email_verification_result)

    saved_email_result: Optional[Dict[str, Any]] = result_service.get_email_result(email_to_verify)
    logging.info('Saved Email Result: {result}'.format(result=saved_email_result))

    domain_search_result: Optional[Dict[str, Any]] = client.domain_search(domain_to_search)

    result_service.add_domain_result(domain_to_search, domain_search_result)

    saved_domain_result: Optional[Dict[str, Any]] = result_service.get_domain_result(domain_to_search)
    logging.info('Saved Domain Result: {result}'.format(result=saved_domain_result))
