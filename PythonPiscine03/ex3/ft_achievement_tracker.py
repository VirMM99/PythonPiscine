

import random

# Global list of acievements
achievements = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder"
]


# To generate a player's achievements
def gen_player_achievements():
    count = random.randint(4, len(achievements))
    selected = random.sample(achievements, count)
    return set(selected)


# Create players
alice = gen_player_achievements()
bob = gen_player_achievements()
charlie = gen_player_achievements()
dylan = gen_player_achievements()

# All achievements
all_achievements = alice.union(bob, charlie, dylan)

# Common Achivements
common_achievements = alice.intersection(bob, charlie, dylan)

# Unique achievements
only_alice = alice.difference(bob.union(charlie, dylan))
only_bob = bob.difference(alice.union(charlie, dylan))
only_charlie = charlie.difference(bob.union(alice, dylan))
only_dylan = dylan.difference(bob.union(alice, charlie))

# Missing achievemments
missing_alice = all_achievements.difference(alice)
missing_bob = all_achievements.difference(bob)
missing_charlie = all_achievements.difference(charlie)
missing_dylan = all_achievements.difference(dylan)


if __name__ == '__main__':
    print("=== Achievement Tracker System ===")
    print(f"\nPlayer Alice: {gen_player_achievements()}")
    print(f"Player Bob: {gen_player_achievements()}")
    print(f"Player Charlie: {gen_player_achievements()}")
    print(f"Player Dylan: {gen_player_achievements()}")
    print(f"\nAll distinct achievements: {all_achievements}")
    print(f"\nCommon achievements: {common_achievements}")
    print(f"\nOnly Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print(f"\nAlice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_charlie}")
    print(f"Dylan is missing: {missing_dylan}")
