# Architecture Notes

## Principle

The backend owns the truth.

That means:
- the browser sends requests
- the Python app validates those requests
- the Python app changes the database
- the browser only displays results

The browser is never trusted to decide:
- damage dealt
- loot earned
- gold gained
- item ownership
- equipped state
- final character stats

## Trust Boundaries

### Client

The browser is a user interface only.
Users can inspect it, replay requests, and tamper with form data.

### Backend

The backend is the authority.
It validates input, applies game rules, and writes safe state changes.

### Database

The database stores persistent state.
Only the backend should write game state.
The browser should never talk directly to the production database.

## Layers

### Web Layer

This will eventually live in `src/dungeon_crawler/web/`.
Its job is to:
- define routes
- read form input
- call systems
- return HTML

Route handlers should stay thin.
They should not contain game rules.

### Systems Layer

This is where the game rules live.
Examples:
- create character
- equip item
- roll encounter
- award loot

This is the most important layer for correctness and future testing.

### Database Layer

This stores persistent data.
Examples:
- users
- characters
- items
- inventory
- audit-friendly history later if needed

## Why This Matters

If route handlers contain all the logic, the project becomes harder to test and harder to understand.

If systems do the real work, then:
- tests are easier
- web routes stay small
- security checks have one place to live
- future Go services can call the same ideas through APIs