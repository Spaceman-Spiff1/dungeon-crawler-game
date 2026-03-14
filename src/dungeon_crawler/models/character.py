from dataclasses import dataclass


@dataclass
class Character:
    name: str
    character_class: str
    strength: int
    intelligence: int
    dexterity: int
    luck: int
    health: int
    mana: int = 0