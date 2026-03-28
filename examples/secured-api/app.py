from fastapi import FastAPI, Request
from middleware.python.sanitizer import sanitize_input
from middleware.python.guardrails import validate_output

app = FastAPI()

SYSTEM_PROMPT = "You are a helpful assistant."

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    user_input = data.get("prompt", "")

    try:
        # ✅ Input validation
        clean_input = sanitize_input(user_input)

        full_prompt = SYSTEM_PROMPT + "\nUser: " + clean_input

        # Simulated LLM response
        response = f"Processed: {clean_input}"

        # ✅ Output validation
        safe_output = validate_output(response)

        return {"response": safe_output}

    except Exception as e:
        return {"error": str(e)}
