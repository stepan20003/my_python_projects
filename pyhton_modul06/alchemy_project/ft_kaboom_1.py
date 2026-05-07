print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
from alchemy.grimoire import dark_spellbook
print(f"Testing record light spell: {dark_spellbook.dark_spell_record('Fantasy','frogs, wind and fire')}")