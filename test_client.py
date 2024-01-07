"""Demonstrate email verification in the main module."""
import logging
from typing import Optional

from email_verifier import EmailVerifier
from service import EmailVerifierService

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Set up the main function to demonstrate email verification."""
    api_key: str = '9ad67b74ed2d3fb60d5cb68ee7a209098c8ae601'
    verifier: EmailVerifier = EmailVerifier(api_key)
    service: EmailVerifierService = EmailVerifierService(verifier)

    email_to_verify: str = 'zhoritihon@gmail.com'
    verification_result: Optional[dict] = verifier.verify_email(email_to_verify)

    if verification_result:
        process_verification_result(service, verification_result)
    else:
        logging.error('Failed to verify email.')


def process_verification_result(service: EmailVerifierService, verification_result: dict) -> None:
    """Process and log email verification results."""
    service.get_results_manager().create_result(verification_result)
    log_info = 'Email verification result: {result}'.format(result=verification_result)
    logging.info(log_info)


if __name__ == '__main__':
    main()
