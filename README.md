# AI API Security Lab

Companion toolkit for the book  
**API Security for AI Applications: Practical Defense Strategies for LLMs, Prompt Injection, and Data Leakage**

---

## What This Is

This is a hands-on lab to test, break, and secure AI APIs.

Not theory. Not slides. Actual scripts and configs you can run.

---

## What You Can Do

- Run prompt injection attacks
- Scan your API for vulnerabilities
- Test input validation failures
- Simulate real-world abuse cases
- Fix issues using middleware templates

---

## Tools Included

- OWASP ZAP (automated scanning)
- Burp Suite Community (manual testing)
- Semgrep (code analysis)
- Docker (isolated test environment)

---

## Quick Start

```bash
git clone https://github.com/yourname/ai-api-security-lab
cd ai-api-security-lab
docker-compose up
````

Run your first attack:

```bash
python prompt-injection/scripts/basic_injection.py
```

---

## Folder Guide

* `/prompt-injection` → attack scripts
* `/middleware` → defense code
* `/zap` → automated scanning
* `/burp` → manual testing
* `/semgrep` → static analysis
* `/threat-modeling` → templates

---

## Important

If your API does not break during testing, you probably didn’t test hard enough.

---

## 📘 Read the Book

This repo is designed to be used with:

**API Security for AI Applications: Practical Defense Strategies for LLMs, Prompt Injection, and Data Leakage**

The book explains *why things break*.
This lab shows you *how they break and how to fix them*.

---
