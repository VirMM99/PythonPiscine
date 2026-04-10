

import random

print("=== Game Data Alchemist ===")

players = [
    'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
    'Gregory', 'john', 'kevin', 'Liam']
print(f"\nInitial list of players: {players}")

# All names Capitalized
all_caps = [name.capitalize() for name in players]
print(f"New list with all names capitalized: {all_caps}")
# Only already capitalized names
capitalize_only = [name for name in players if name[0].isupper()]
print(f"New list of capitalized names only: {capitalize_only}")
# Dictionary with random scores
scores = {name: random.randint(0, 1000) for name in all_caps}
print(f"\nScore dict: {scores}")
# Average Score
average = round(sum(scores.values()) / len(scores), 2)
print(f"Score average is {average}")
# High scores
high_scores = {
    name: score for name, score in scores.items() if score > average}
print(f"High scores: {high_scores}")
