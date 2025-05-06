#!/bin/bash
docker run --rm -v $(pwd):/project aquasec/trivy fs /project --format json --output trivy_report.json