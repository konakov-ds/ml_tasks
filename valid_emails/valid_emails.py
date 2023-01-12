from typing import List
import re

# fastest version with compile
def valid_emails(strings: List[str]) -> List[str]:
    """
    Take list of potential emails
    and returns only valid ones
    """

    valid_email_regex = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    email_regex_compiled = re.compile(valid_email_regex)

    def is_valid_email(email: str) -> bool:
        return bool(email_regex_compiled.fullmatch(email))

    emails = []
    for email in strings:
        if is_valid_email(email):
            emails.append(email)

    return emails