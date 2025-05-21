#!/bin/bash
set -eo pipefail

CRITICALITY=$(jq -r '.criticality' ai_response.json)

if (( $(echo "$CRITICALITY >= $THRESHOLD" | bc -l) )); then
   echo "Criticality $CRITICALITY exceeds threshold $THRESHOLD"
   exit 1
else
   echo "Vulnerabilities within acceptable range"
   exit 0
fi
