#!/bin/bash
set -eo pipefail

# Install Trivy
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Run scan
trivy fs --format json --output trivy-report.json ./app

# Debug output
echo "Trivy scan completed. Report generated."