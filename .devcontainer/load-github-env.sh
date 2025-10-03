#!/bin/bash
# Early GitHub Environment Loader
# Ensures GITHUB_USER is available as early as possible for terminal prompt

# Only run if GITHUB_USER is not already set
if [ -z "${GITHUB_USER:-}" ] && [ -f "/workspaces/.codespaces/shared/.env-secrets" ]; then
    # Load GitHub environment variables from codespaces secrets
    while read line; do
        if [ ! -z "$line" ]; then
            key=$(echo $line | sed "s/=.*//")
            value=$(echo $line | sed "s/$key=//1")
            decodedValue=$(echo $value | base64 -d 2>/dev/null)
            if [ ! -z "$decodedValue" ] && [ "$key" = "GITHUB_USER" ]; then
                export GITHUB_USER="$decodedValue"
                break
            fi
        fi
    done < /workspaces/.codespaces/shared/.env-secrets
fi