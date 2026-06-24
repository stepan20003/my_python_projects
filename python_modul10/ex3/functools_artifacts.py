from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == 'max':
        return reduce(max, spells)
    if operation == 'min':
        return reduce(min, spells)
    try:
        name = getattr(operator, operation)
        result = reduce(name, spells)
    except Exception as e:
        print(e)
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    lightning = partial(base_enchantment, 50, "lightning")
    return {"fire": fire, "ice": ice, "lightning": lightning}


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} is enchanted with {element} power {power}"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n-1)+memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast_spell(target: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register
    def _(target: str) -> str:
        return f"Enchatment: {target}"

    @cast_spell.register
    def _(target: int) -> str:
        return f"Damage spell: {target} damage"

    @cast_spell.register
    def _(target: list) -> str:
        return f"Multi-cast: {len(target)} spells"
    return cast_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([30,40,30],'add')}")
    print(f"Product: {spell_reducer([100, 2400],'mul')}")
    print(f"Max: {spell_reducer([20,40,4],'max')}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    print("Testing spell dispatcher...")
    foo = spell_dispatcher()
    print(foo(42))
    print(foo('fireball'))
    print(foo([10, 20, 39]))
    print(foo({"Security": 100}))
