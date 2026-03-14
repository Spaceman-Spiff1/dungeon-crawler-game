# Dungeon Crawler Game

A fresh, structured restart of an older Python learning project, now organized as a learning-first web app project.

## Project Style

This repo is meant to feel like a school project:
- small steps
- clear explanations
- frequent commits
- feature branches and pull requests
- simple architecture before clever architecture
- local understanding before cloud deployment

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

## Working Rules

- Keep pull requests small
- Keep logic in Python modules, not directly in route handlers
- Treat the browser as untrusted
- Make the backend the source of truth
- Do not let the client calculate rewards, loot, or final game state
- Prefer code that is easy to explain over code that is fancy
- Use a project-local virtual environment for all Python work

## Python Environment Rule

All Python development in this repository must be performed inside a project-local virtual environment named `.venv`.

Do not:
- install project packages globally
- run tests outside the virtual environment
- assume system Python matches the project environment

## Windows Setup

From PowerShell in the project root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

If PowerShell blocks activation, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Deactivate later with:

```powershell
deactivate
```

## Preferred Dev Environment

For long-term development, WSL2 with Ubuntu is recommended because it provides a more Linux-like environment for Python, Git, containers, and Kubernetes work.

If using WSL2, prefer keeping the repo inside the Linux filesystem, for example:

```bash
~/projects/dungeon-crawler-game
```

## Git And GitHub Workflow

We are using GitHub to practice professional habits, not just as backup.

Typical workflow:

```powershell
git checkout -b feat/character-save
# make a small change
git add .
git commit -m "Add character save flow"
git push -u origin feat/character-save
```

Then open a pull request into `main`.

Guidelines:
- one branch per task
- one pull request per focused change
- merge only when the change is understood
- keep secrets out of the repo

## First Milestone

Make one local user flow work end to end:
- create a character
- save it to SQLite
- load it back
- prove it with a test

Do not add login, cloud deployment, or GKE work in this milestone.

## Testing Plan

Automated testing should stay small and free.

The current direction is:
- run tests locally inside `.venv`
- later add GitHub Actions for free pull request and push checks
- keep CI simple at first: install dependencies and run `pytest`

## Cloud Direction

Cloud work comes later.

Planned order:
1. local Python + SQLite
2. small web app
3. auth and ownership checks
4. manual Cloud Run deployment
5. GitHub-to-GCP integration
6. GKE as a temporary learning lab, not the first production target

## Security Basics

Even in a tiny game, assume the client can lie.

That means the backend must decide:
- what a player owns
- whether an item can be equipped
- whether an encounter result is valid
- whether a character belongs to the logged-in user

## Next Step

Finish Milestone 1 in a way that is easy to explain:
- build character creation
- save to SQLite
- load from SQLite
- add tests
- walk through each file and why it exists