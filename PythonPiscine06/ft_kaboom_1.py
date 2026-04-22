
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


def do_it():
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print(dark_spell_record("Fantasy", "bats, frogs, arsenic"))


do_it()
