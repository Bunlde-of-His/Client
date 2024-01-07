"""Module for defining the EmailVerifierService class."""
from typing import Optional, List, Dict

from email_verifier import EmailVerifier


class VerificationResultManager(object):
    """Manager for storing and managing verification results."""

    def __init__(self) -> None:
        """Initialize the VerificationResultManager."""
        self.verification_results: List[Dict] = []

    def get_results(self) -> List[Dict]:
        """Get all stored verification results."""
        return self.verification_results

    def clear_results(self) -> None:
        """Clear all stored verification results."""
        self.verification_results = []

    def create_result(self, new_result: Dict) -> None:
        """Create a new verification result and store it."""
        self.verification_results.append(new_result)

    def read_results(self) -> List[Dict]:
        """Read all stored verification results."""
        return self.verification_results

    def update_result(self, index: int, new_result: Dict) -> bool:
        """Update a stored verification result."""
        if 0 <= index < len(self.verification_results):
            self.verification_results[index] = new_result
            return True
        return False

    def delete_result(self, index: int) -> bool:
        """Delete a stored verification result."""
        if 0 <= index < len(self.verification_results):
            self.verification_results.pop(index)
            return True
        return False


class EmailVerifierService(object):
    """Service for verifying and storing email verification results."""

    def __init__(self, email_verifier_client: EmailVerifier) -> None:
        """Initialize the EmailVerifierService instance."""
        self.email_verifier_client: EmailVerifier = email_verifier_client
        self.result_manager = VerificationResultManager()

    def verify_and_store_email(self, email: str) -> bool:
        """Verify the provided email and store the result."""
        verification_result: Optional[Dict] = self.email_verifier_client.verify_email(email)
        if verification_result:
            self.result_manager.create_result(verification_result)
            return True
        return False

    def get_results_manager(self) -> VerificationResultManager:
        """Get the manager for verification results."""
        return self.result_manager
