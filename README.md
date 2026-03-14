# Dungeon Crawler Game

A fresh, structured restart of an older Python learning project, now organized as a learning-first web app project.

## Project Style

This repo is meant to feel like a school project:
- small steps
- clear explanations
- frequent commits
- feature branches and pull requests
- simple architecture before clever architecture

## Current Goal

Build a very small Python app in safe stages:
1. create and save a character locally
2. load and display that character
3. add a basic web interface
4. add login only after the app has a safe backend flow
5. deploy only after the local app is understandable

## Learning Roadmap

Read these in order:
1. `docs/course_plan.md`
2. `docs/fundamentals.md`
3. `docs/architecture.md`
4. `docs/security_baseline.md`
5. `docs/github_workflow.md`
6. `docs/roadmap.md`

## Project Layout

```text
dungeon_crawler_game/
+- .github/               # Pull request templates and later CI
+- data/                  # Local SQLite database and dev data
+- docs/                  # Notes, lessons, and plans
+- src/
¦  +- dungeon_crawler/
¦     +- cli/             # Temporary command-line entry points
¦     +- db/              # Database connection and schema helpers
¦     +- models/          # Core data objects
¦     +- systems/         # Game rules and business logic
¦     +- web/             # Future Flask web routes and templates
+- tests/                 # Automated tests
+- .gitignore
+- pyproject.toml
```

## First Milestone

Make one local user flow work end to end:
- create a character
- save it to SQLite
- load it back
- prove it with a test

Do not add login, cloud deployment, or GKE work in this milestone.

## Working Rules

- Keep pull requests small
- Keep logic in Python modules, not directly in route handlers
- Treat the browser as untrusted
- Make the backend the source of truth
- Do not let the client calculate rewards, loot, or final game state
- Prefer code that is easy to explain over code that is fancy