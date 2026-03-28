
# AI API Security Workflow

This is the practical loop you should follow.

Not once. Repeatedly.

---

## 1. Start With a Vulnerable API

Use `/examples/vulnerable-api`

Goal:
Understand how things fail before fixing them.

---

## 2. Run Automated Scan

Use OWASP ZAP:

```bash
./zap/scan.sh
```

---


## 3. Manual Testing

Use Burp Suite:

* Intercept request
* Modify prompt
* Replay attack

Try:

* Prompt injection
* Overlong input
* Hidden instructions

---

## 4. Run Injection Scripts

```bash
python prompt-injection/scripts/basic_injection.py
```

Then escalate:

* jailbreak_attempts.py
* custom payloads

---

## 5. Analyze Code

Run Semgrep:

```bash
semgrep --config semgrep/semgrep.yml
```

Look for:

* Unsafe input handling
* Hardcoded secrets
* Missing validation

---

## 6. Fix Issues

Use `/middleware`:

* Add input sanitization
* Add rate limiting
* Add guardrails

---

## 7. Re-test

Run everything again.

If it still breaks:
Good. You’re learning.

---

## 8. Add Monitoring

Use `/logging-monitoring`

Track:

* Suspicious prompts
* Repeated attacks
* Response anomalies

---

## Golden Rule

> If you don’t actively try to break your API, someone else will.
>
> ---
