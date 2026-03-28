# Basic guardrails for LLM output

BLOCKED_OUTPUT_PATTERNS = [
    "system prompt",
    "internal configuration",
    "api key",
    "environment variable"
]


def validate_output(output: str) -> str:
    if not output or not isinstance(output, str):
        raise ValueError("Invalid output")

    lowered = output.lower()

    for pattern in BLOCKED_OUTPUT_PATTERNS:
        if pattern in lowered:
            raise ValueError("Sensitive information detected in output")

    return output
