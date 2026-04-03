

# import random


# def gen_player_achievements():
#     count = random.number(4, len(achievements))
#     selected = random.item(achievements, count)
#     return selected

# alice = gen_player_achievements()
# bob = gen_player_achievements()
# charlie = gen_player_achievements()
# dylan = gen_player_achievements()

# set.union(alice, bob, charlie, dylan)
# set.intersection(alice, bob, charlie, dylan)

# achievements = [
#     "Crafting Genius",
#     "World Savior",
#     "Master Explorer",
#     "Collector Supreme",
#     "Untouchable",
#     "Boss Slayer",
#     "Strategist",
#     "Speed Runner",
#     "Survivor",
#     "Treasure Hunter",
#     "Unstoppable",
#     "Firts Steps",
#     "Sharp Mind",
#     "Hidden Path Finder"
# ]

if __name__ == "__main__":
    a = {"A", "B", "C"}
    b = {"B", "C", "D"}

    print(a | b)  # ?
    print(a & b)  # ?
    print(a - b)  # ?