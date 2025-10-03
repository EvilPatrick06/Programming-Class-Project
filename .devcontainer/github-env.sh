# GitHub Codespaces Early Environment Setup
# This file is sourced early in shell initialization to ensure
# GitHub environment variables are available for the terminal prompt

# Load GitHub environment if not already set
if [ -z "${GITHUB_USER:-}" ] && [ -f "/workspaces/.codespaces/shared/.env-secrets" ]; then
    while read line; do
        if [ ! -z "$line" ]; then
            key=$(echo $line | sed "s/=.*//")
            value=$(echo $line | sed "s/$key=//1")
            decodedValue=$(echo $value | base64 -d 2>/dev/null)
            if [ ! -z "$decodedValue" ]; then
                export $key="$decodedValue"
            fi
        fi
    done < /workspaces/.codespaces/shared/.env-secrets
fi