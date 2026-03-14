from dungeon_crawler.systems.character_creation import build_character


def test_build_character_returns_expected_class() -> None:
    character = build_character("Aria", "Mage")

    assert character.name == "Aria"
    assert character.character_class == "Mage"
    assert character.mana >= 10