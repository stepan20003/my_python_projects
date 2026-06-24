from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (
            spell1(target, power),
            spell2(target, power)
            )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifer(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifer


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [
            spell(target, power)
            for spell in spells
        ]
    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    spell = spell_combiner(fireball, heal)
    print(spell("Dragon", 20))
    print("Testing power amplifier...")
    amplifier = power_amplifier(heal, 5)
    print(amplifier("Dragon", 10))
    print("Testing conditional caster...")
    caster = conditional_caster(fireball, heal)
    print(caster("dragon", 30))
    print("Testing spell sequence...")
    lst1 = [fireball, heal]
    sequence = spell_sequence(lst1)
    print(sequence("Dragon", 60))
