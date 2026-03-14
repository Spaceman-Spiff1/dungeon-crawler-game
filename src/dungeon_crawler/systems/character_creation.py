import random

from dungeon_crawler.models.character import Character


def build_character(name: str, character_class: str) -> Character:
    strength = random.randint(1, 10)
    intelligence = random.randint(1, 10)
    dexterity = random.randint(1, 10)
    luck = random.randint(1, 10)
    health = strength + intelligence
    mana = intelligence + 10 if character_class.lower() == "mage" else 0

    return Character(
        name=name,
        character_class=character_class,
        strength=strength,
        intelligence=intelligence,
        dexterity=dexterity,
        luck=luck,
        health=health,
        mana=mana,
    )