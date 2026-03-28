# AI Threat Model Template

Use this before building OR after things break.

---

## 1. System Overview

Describe:
- What your API does
- What model it uses
- Who can access it

---

## 2. Entry Points

- API endpoints
- Prompt inputs
- File uploads
- Internal system prompts

---

## 3. Assets to Protect

- API keys
- System prompts
- User data
- Logs
- Model outputs

---

## 4. Threats

| Threat | Description |
|------|------------|
| Prompt Injection | Malicious input overriding instructions |
| Data Leakage | Sensitive info exposed |
| Abuse | Excessive usage |
| Logging Leak | Secrets stored in logs |

---

## 5. Attack Paths

Example:

User Input → Prompt → LLM → Response → Logs

Where can it fail?

---

## 6. Controls

| Area | Control |
|------|--------|
| Input | Sanitization |
| Output | Filtering |
| Usage | Rate limiting |
| Logs | Masking |

---

## 7. Testing Plan

- Run injection scripts
- Use Burp Suite
- Run ZAP scan

---

## Final Thought

If you didn’t model the threat…

You already missed something.
