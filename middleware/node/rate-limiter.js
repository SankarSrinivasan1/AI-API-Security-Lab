// Simple in-memory rate limiter (good enough for demo, not production)

const requests = new Map();

const WINDOW_SIZE_MS = 60 * 1000; // 1 minute
const MAX_REQUESTS = 10;

function rateLimiter(ip) {
  const now = Date.now();

  if (!requests.has(ip)) {
    requests.set(ip, []);
  }

  const timestamps = requests.get(ip);

  // Remove old requests
  const filtered = timestamps.filter(ts => now - ts < WINDOW_SIZE_MS);
  filtered.push(now);

  requests.set(ip, filtered);

  if (filtered.length > MAX_REQUESTS) {
    throw new Error("Rate limit exceeded");
  }

  return true;
}

module.exports = rateLimiter;
