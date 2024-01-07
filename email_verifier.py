"""Module for email verification."""
import logging
from typing import Optional

import requests

logging.basicConfig(level=logging.INFO)


class EmailVerifier(object):
    """Class for verifying email using Hunter.io API."""

    def __init__(self, api_key: str) -> None:
        """Initialize the EmailVerifier instance."""
        self.api_key = api_key
        self.api_url = 'https://api.hunter.io/v2/email-verifier'

    def verify_email(self, email: str) -> Optional[dict]:
        """Verify the provided email using the Hunter.io API.

        Args:
            email (str): The email address to be verified.

        Returns:
            Optional[dict]: A dictionary containing the verification results,
            or None if an error occurs during the API request.
        """
        request_params = {'email': email, 'api_key': self.api_key}

        try:
            response = requests.get(self.api_url, params=request_params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as request_error:
            logging.error('Error during API request: {error}'.format(error=request_error))
            return None
