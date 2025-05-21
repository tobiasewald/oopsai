#!/bin/bash
set -eo pipefail

# Download OWASP DC
curl -LO https://github.com/jeremylong/DependencyCheck/releases/download/v8.3.1/dependency-check-8.3.1-release.zip
unzip dependency-check-8.3.1-release.zip

# Run scan
./dependency-check/bin/dependency-check.sh \
  --project "oops.ai" \
  --scan . \
  --format JSON \
  --out dependency-check-report.json \
  --disableCentral \
  --disableAssembly

echo "OWASP scan completed. Report generated."