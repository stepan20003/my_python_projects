def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifacts: artifacts["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
        lambda mages: mages["power"] >= min_power,
        mages
    ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda spell: f"* {spell} *",
        spells
    ))


def mage_stats(mages: list[dict]) -> dict:
    result = list(map(lambda mage: mage["power"], mages))
    return {"max_power": max(result),
            "min_power": min(result),
            "avg_power": round(sum(result)/len(result), 2)}


if __name__ == "__main__":
    artifacts_data = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Shadow Dagger", "power": 78, "type": "dagger"}
    ]

    mages_data = [
        {"name": "Merlin", "power": 95, "element": "fire"},
        {"name": "Luna", "power": 72, "element": "water"},
        {"name": "Drake", "power": 88, "element": "earth"}
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")

    sorted_artifacts = artifact_sorter(artifacts_data)

    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) "
        f"comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )
    print("\nTesting power filter...")
    filtered_mages = power_filter(mages_data, 80)

    for mage in filtered_mages:
        print(f"{mage['name']} - {mage['power']}")

    print("Testing spell transformer...")

    transformed = spell_transformer(spells)

    print(*transformed)
    print("\nTesting mage stats...")
    stats = mage_stats(mages_data)

    print(stats)
