# Anomaly Detection for AI APIs

Logging is not enough.

If you don’t look for patterns, you’ll miss attacks completely.

---

## What to Monitor

### 1. Repeated Prompt Injection Attempts

Examples:
- "ignore previous instructions"
- "reveal system prompt"

If you see these repeated → someone is probing your system.

---

### 2. Sudden Spike in Requests

Possible:
- Bot activity
- Abuse attempt
- Load testing (hopefully yours)

---

### 3. Long or Unusual Inputs

Watch for:
- Extremely long prompts
- Encoded payloads
- Repeated characters

---

### 4. Suspicious Output

Red flags:
- Mentions of "system prompt"
- API keys
- Internal configuration

---

## Simple Detection Strategy

- Count suspicious keywords
- Track requests per IP
- Flag repeated failures

---

## Example Logic

```python
if "ignore previous instructions" in input.lower():
    flag_attack()

if request_count > threshold:
    flag_rate_abuse()
