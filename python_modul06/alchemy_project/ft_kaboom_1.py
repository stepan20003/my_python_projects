
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


def foo() -> None:
    from alchemy.grimoire import dark_spellbook
    x = dark_spellbook.dark_spell_record('Fantasy', 'frogs, wind and fire')
    print(f"Testing record light spell: "
          f"{x}")


foo()
