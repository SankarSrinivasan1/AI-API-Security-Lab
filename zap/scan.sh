#!/bin/bash

# Simple OWASP ZAP scan script
# Runs a baseline scan against the API

TARGET=${1:-http://api:8000}

echo "Starting ZAP scan on $TARGET"

docker run --rm -v $(pwd):/zap/wrk/:rw \
  owasp/zap2docker-stable zap-baseline.py \
  -t $TARGET \
  -g gen.conf \
  -r zap-report.html

echo "Scan complete. Report saved as zap-report.html"
