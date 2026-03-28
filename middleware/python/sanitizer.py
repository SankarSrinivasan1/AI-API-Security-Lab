# Basic input sanitizer for AI prompts

import re

BLOCKED_PATTERNS = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"show hidden instructions",
    r"bypass restrictions",
    r"debug mode",
    r"print internal"
]

MAX_LENGTH = 5000


def sanitize_input(user_input: str) -> str:
    if not user_input or not isinstance(user_input, str):
        raise ValueError("Invalid input")

    if len(user_input) > MAX_LENGTH:
        raise ValueError("Input too long")

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            raise ValueError("Potential prompt injection detected")

    return user_input
