# Fundamentals

## What This Project Is

This game is easiest to understand as four layers:

1. `models`
   These are the nouns in the game: character, item, inventory entry, room, enemy.

2. `systems`
   These are the rules: character creation, combat, leveling, loot drops, equipment.

3. `db`
   This is persistence. It stores characters, items, and inventory so progress survives after the program exits.

4. `web`
   This will become the player interface. It will collect input and show output, but it will not own game rules.

## Why The Database Matters

Without a database, the game only exists while the script is running.

With a database, you can:
- save characters
- save inventories and equipped gear
- look up items by type or rarity
- load an old game later
- eventually support multiple characters or parties

SQLite is the right starting point because it is built into Python and does not need a server.

## Core Data You Need

At minimum, the game should track:

### Characters
- id
- owner_user_id later
- name
- class
- strength
- intelligence
- dexterity
- luck
- health
- mana

### Items
- id
- name
- slot
- rarity
- stat bonuses

### Inventory
- which character owns which item
- whether the item is equipped

## Recommended Build Order

1. Character creation
   Start with creating a character in Python and saving it to the database.

2. Character loading
   Load the same character back and prove the data round-trips correctly.

3. Web page
   Put the same flow behind a very small web form.

4. Auth
   Add login only after the backend can already enforce safe ownership rules.

5. Encounters and progression
   Add rooms, enemies, loot, gold, and leveling after the basic data flow is stable.

## Difference Between Models And Systems

A good rule:

- A model holds data.
- A system changes data.

Example:
- `Character` is a model.
- `build_character()` is a system.
- `equip_item()` would also be a system.

That split keeps the project easier to read and test.

## Security Mindset

Even in a tiny game, assume the client can lie.
That means the backend must decide:
- what a user owns
- whether an item can be equipped
- whether an encounter result is valid
- whether a character belongs to the logged-in user

## What To Keep From The Old Prototype

Your old work already had the right instincts:
- start with a base character class
- add specialized classes like mage
- generate stats
- build a party or crew

The main improvement now is separating game rules from storage and organizing the files so each part has one job.