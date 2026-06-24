from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulator(power: int) -> int:
        nonlocal total
        total += power
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchat(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchat


def memory_vault() -> dict[str, Callable]:
    my_dict = {}

    def store(key: str, value: int) -> dict:
        my_dict.update({key: value})
        return my_dict

    def recall(key: str) -> dict[Any, Any] | str | int:
        if key in my_dict:
            return my_dict[key]
        return "Memory not found"
    return {"Store": store, "Recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    a = mage_counter()
    b = mage_counter()
    print(f"counter_a call 1: {a()}")
    print(f"counter_a call 1: {a()}")
    print(f"counter_b call 1: {b()}\n")
    base = spell_accumulator(100)
    print("Testing spell accumulator...")
    print(f"Base 100, add 20: {base(20)}")
    print(f"Base 100, add 20: {base(30)}\n")
    print("Testing enchantment factory...")
    sword = enchantment_factory("Flaming")
    shield = enchantment_factory("Frozen")
    print(sword("Sword"))
    print(f"{shield('Shield')}\n")
    print("Testing memory vault...")
    dict1 = memory_vault()
    store = dict1["Store"]
    store("secret", 42)
    recall = dict1["Recall"]
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")
