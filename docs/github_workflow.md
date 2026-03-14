# GitHub Workflow

## Why Use GitHub Here

GitHub is not just backup.
It is where we practice professional habits:
- feature branches
- pull requests
- code review
- merge discipline
- release history

## Small Branch Strategy

Use one branch per task.

Examples:
- `feat/character-save`
- `feat/web-create-character`
- `feat/add-local-login`
- `docs/project-overview`
- `fix/schema-bug`

## Pull Request Rules

Every pull request should do one job.

Good examples:
- add character repository code
- add first web route
- add tests for item creation

Avoid mixing these into one PR:
- schema changes
- route refactors
- CSS cleanup
- docs rewrite
- deployment automation

## Commit Style

Use small commits with clear messages.

Examples:
- `Add character dataclass`
- `Create SQLite schema initializer`
- `Add PR template for learning workflow`

## PR Review Checklist

Before merging, check:
- does the code solve one clear problem?
- can we explain how it works?
- are there tests or at least a manual test plan?
- is any logic stuck in the wrong layer?
- did we keep secrets out of the repo?
- does the backend re-check any user-controlled input?

## Suggested GitHub Setup

Once your GitHub repo exists:
- protect the `main` branch
- require pull requests before merge
- optionally require one approval, even if you are practicing solo
- add a PR template
- later add GitHub Actions or Cloud Build checks

## GCP Link

Yes, GitHub can link with GCP.

Use that connection carefully.

The smallest good deployment path is:
- push code to GitHub
- review and merge to `main`
- deploy manually from a known-good commit at first
- add automated deployment only after tests and rollback steps exist

Avoid deploying every pull request automatically in the early phases.
That creates too much risk and makes the learning loop harder to control.