# AI Threat Modeling Guide

Most developers skip this.

Then they wonder why their API leaks data.

---

## Step 1: Identify Entry Points

Where can users interact?

- API endpoints
- Prompt inputs
- File uploads
- System instructions

---

## Step 2: Identify Assets

What needs protection?

- API keys
- System prompts
- User data
- Model outputs

---

## Step 3: Identify Threats

Common AI threats:

- Prompt Injection
- Data Exfiltration
- Model Abuse
- Token Flooding
- Logging Sensitive Data

---

## Step 4: Map Attack Paths

Example:

User Input → Prompt → LLM → Response → Logs

Where can it break?

- Input not validated
- Output not filtered
- Logs storing secrets

---

## Step 5: Add Controls

For each threat:

| Threat | Control |
|------|--------|
| Prompt Injection | Input filtering |
| Data Leakage | Output filtering |
| Abuse | Rate limiting |
| Logging leaks | Mask sensitive data |

---

## Step 6: Test It

Use:
- prompt-injection scripts
- Burp Suite
- ZAP scans

---

## Common Mistakes

- Trusting LLM output blindly
- Logging everything “for debugging”
- No rate limits
- No input validation

---

## Simple Rule

Treat AI input like SQL input.

Never trust it.
