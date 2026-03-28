// Basic input sanitization for AI prompts

function sanitizeInput(input) {
  if (!input || typeof input !== "string") {
    throw new Error("Invalid input");
  }

  const blockedPatterns = [
    /ignore previous instructions/i,
    /reveal system prompt/i,
    /show hidden instructions/i,
    /bypass restrictions/i,
    /debug mode/i,
    /print internal/i
  ];

  for (let pattern of blockedPatterns) {
    if (pattern.test(input)) {
      throw new Error("Potential prompt injection detected");
    }
  }

  // Optional: trim excessively long input
  if (input.length > 5000) {
    throw new Error("Input too long");
  }

  return input;
}

module.exports = sanitizeInput;
