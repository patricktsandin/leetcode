"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period '.' with '[.]'.
"""


class Solution:
    """Solves in linear time and space using an iterative algorithm."""

    @staticmethod
    def defang_ip_address(address: str) -> str:
        """Return an IPv4 address, surrounding all separators
        with brackets."""
        return ''.join(
            [
                char if char != '.' else '[.]'
                for char in address
            ]
        )
