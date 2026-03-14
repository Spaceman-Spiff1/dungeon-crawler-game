# AGENTS.md

## Project Mode

This repository is a learning-first project.
Work should feel like a school project:
- small steps
- clear explanations
- simple architecture
- local development before cloud deployment

## Python Rule

All Python work in this repository must use a project-local virtual environment named `.venv`.

Before running Python commands:
1. create `.venv` if it does not exist
2. activate `.venv`
3. install packages only inside `.venv`

Do not:
- install project dependencies globally
- run tests outside `.venv`
- assume system Python is correct for the project

## Development Priority

Build in this order:
1. local Python logic
2. SQLite persistence
3. small web interface
4. auth and ownership checks
5. Cloud Run deployment
6. GKE as a temporary learning lab

Do not jump ahead to GKE or production automation before the local app is understandable.

## Security Rules

- Treat the browser as untrusted.
- The backend is the source of truth.
- The client must not decide loot, rewards, ownership, or final game state.
- Keep secrets out of the repository.
- Do not enable automatic production deployment from pull requests.

## Git Workflow

- Use one branch per task.
- Keep pull requests small.
- Prefer changes that are easy to explain.
- Add or update docs when the workflow changes.

## Testing Rule

For new Python behavior:
- prefer adding or updating tests
- run tests locally inside `.venv`
- keep automated checks simple and free

## Teaching Style

When explaining code or changes:
- explain what the file does
- explain why it exists
- explain how it connects to the rest of the project
- prefer clarity over cleverness