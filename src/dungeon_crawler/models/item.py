from dataclasses import dataclass


@dataclass
class Item:
    name: str
    slot: str
    rarity: str
    strength_bonus: int = 0
    intelligence_bonus: int = 0
    dexterity_bonus: int = 0
    luck_bonus: int = 0
    health_bonus: int = 0
    mana_bonus: int = 0