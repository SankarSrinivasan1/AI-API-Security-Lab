# 🛠 Setup Guide

This guide gets you from “cloned repo” to “breaking your API” in minutes.

---

## 1. Prerequisites

Install:

- Docker
- Docker Compose
- Python 3.9+

Optional (recommended):
- Burp Suite Community Edition
- Node.js (for middleware testing)

---

## 2. Clone the Repo

```bash
git clone https://github.com/yourname/ai-api-security-lab
cd ai-api-security-lab

---

## 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` if needed:

* Add your API keys
* Adjust flags

---

## 4. Start Everything

```bash
docker-compose up --build
```

This will start:

* API server
* Attacker container
* OWASP ZAP (scanner)

---

## 5. Verify API

Open:

```
http://localhost:8000
```

If it loads, you're good.

---

## 6. Run First Attack

```bash
python prompt-injection/scripts/basic_injection.py
```

Expected result:

* Either strange output
* Or system prompt leakage
* Or error (also useful)

---

## Common Issues

### Port already in use

Change port in `.env`

---

### Docker not starting

Restart Docker. Yes, seriously.

---

### Script not working

Check:

* API is running
* URL is correct

---

## Reality Tip

If setup feels too smooth, something is probably misconfigured 🙂

````
