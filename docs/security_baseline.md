# Security Baseline

## Main Risks For This Project

The biggest early risks are not fancy cloud attacks.
They are simple mistakes like:
- trusting browser input
- letting one user read another user's data
- putting game rules inside web forms or JavaScript
- committing secrets to GitHub
- turning on deployment automation too early
- leaving GKE resources running after practice

## Rules We Will Follow

- The backend is authoritative.
- The browser is untrusted.
- No direct browser writes to the production database.
- No secrets in the repo.
- No real cloud deployment until the local flow is understood.
- No automatic production deploys from pull requests.

## Minimum Security Checks

Before adding login:
- the backend must own character creation
- the backend must own stat generation or validation
- tests should cover database round trips

Before adding multi-user support:
- every character must have an owner
- every read and write must verify the owner
- admin actions must stay separate from player actions

Before deploying:
- use environment variables or Secret Manager for secrets
- disable debug settings in production
- log important state changes
- set a billing budget or alert in GCP

## Cost Safety Checks

Cheap systems can still create surprise bills.

We will:
- start locally
- deploy to Cloud Run before trying GKE
- use GKE only as a temporary lab at first
- delete unused cloud resources quickly
- avoid managed services we do not understand yet