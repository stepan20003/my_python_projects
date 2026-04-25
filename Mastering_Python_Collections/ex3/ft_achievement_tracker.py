import random


def gen_player_achievements() -> set:
    all_set = ['Crafting Genius', 'Strategist', 'World Savior'
               'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter'
               'Unstoppable', 'First Steps', 'Collector Supreme'
               'Untouchable', 'Sharp Mind', 'Boss Slayer']
    count = random.randint(1, len(all_set))
    return (set(random.sample(all_set, count)))


def gen_player() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {alice | bob | charlie | dylan}\n")
    print(f"Comon achievements: {alice & bob & charlie & dylan}")
    print(f"Only Alice has: {alice - (bob | charlie | dylan)}")
    print(f"Only Bob has: {bob - (alice | charlie | dylan)}")
    print(f"Only Charlie has: {charlie - (alice | bob | dylan)}")
    print(f"Only Dylan has: {dylan - (alice | charlie | bob)}\n")
    print(f"Alice is missing: {(bob | charlie | dylan) - alice}")
    print(f"Bob is missing: {(alice | charlie | dylan) - bob}")
    print(f"Charlie is missing: {(bob | alice | dylan) - charlie}")
    print(f"Dylan is missing: {(bob | charlie | alice) - dylan}")


if __name__ == "__main__":
    gen_player()
