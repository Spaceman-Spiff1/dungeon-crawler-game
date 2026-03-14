# Course Plan

## Goal

Learn how to build and ship a very small web game like a real software project.

By the end of the early phases, you should understand:
- how the Python app is organized
- how the database stores game state
- how web requests move through the app
- how Git branches and pull requests work
- how GitHub can connect to GCP deployments
- why backend authority matters for security

## Phase 0: Project Setup

What we are doing now:
- create a clean repo structure
- write the learning docs
- define the first milestone
- set up a GitHub workflow that is safe and repeatable

## Phase 1: Python Fundamentals In Context

Build small pieces and explain each one:
- data models
- functions and return values
- imports and packages
- reading and writing SQLite data
- basic tests

Deliverable:
- create and save a character
- load the same character back
- explain every file involved

## Phase 2: Web App Fundamentals

Add a very small Python web app.

Topics:
- routes
- forms
- request and response cycle
- templates
- sessions
- validation

Deliverable:
- user can open a page and create a character from the browser
- the backend still owns all game-state changes

## Phase 3: Auth And Safety Basics

Only add login after the basic app flow is clear.

Topics:
- user accounts
- sessions
- password safety or managed auth
- authorization checks
- protecting one user's data from another user

Deliverable:
- a logged-in user can only access their own characters

## Phase 4: GitHub Workflow

Topics:
- create a branch for each task
- make small commits
- open a pull request
- review the pull request
- merge only when the change is understood

Deliverable:
- one merged pull request for each milestone task

## Phase 5: Cloud Fundamentals

Topics:
- container basics
- environment variables
- secrets
- deployment flow
- logs
- cost guardrails

Deliverable:
- deploy the small Python app to Cloud Run first
- keep deployment manual at first

## Phase 6: GKE Practice Lab

Topics:
- pods
- deployments
- services
- config maps and secrets
- rolling updates
- deleting the cluster when practice is done

Deliverable:
- deploy the same app to a very small GKE lab environment for learning
- do not make GKE the default production target yet

## Rule Of Thumb

If a design makes the project harder to explain, it is probably too complex for the current phase.