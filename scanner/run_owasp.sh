#!/bin/bash
docker run --rm -v $(pwd):/src owasp/dependency-check --scan /src --format JSON --out . --project OopsAI
mv dependency-check-report.json owasp_report.json