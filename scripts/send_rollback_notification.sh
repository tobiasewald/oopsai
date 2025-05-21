#!/bin/sh
set -eo pipefail

CRITICALITY=$(jq -r '.criticality' ai_response.json)
ROLLBACK_INFO=$(kubectl rollout history deployment/$DEPLOYMENT_NAME -n $KUBE_NAMESPACE | tail -2)
COMMIT_AUTHOR=$(git log -1 --pretty=format:'%an')

curl -X POST -H "Content-Type: application/json" -d @- ${DISCORD_WEBHOOK} <<EOF
{
  "content": "🚨🚨 EMERGENCY ROLLBACK EXECUTED 🚨🚨",
  "embeds": [{
    "title": "Rollback Alert!",
    "description": "**Criticality Score**: $CRITICALITY/5\n\n**Last Commit Author**: $COMMIT_AUTHOR\n\n**Rollback Info**:\n\`\`\`$ROLLBACK_INFO\`\`\`",
    "color": 16711680,
    "footer": {
      "text": "Oops.AI Security System"
    }
  }]
}
EOF