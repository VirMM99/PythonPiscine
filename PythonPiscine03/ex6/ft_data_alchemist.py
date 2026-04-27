

import random

print("=== Game Data Alchemist ===")

players: list[str] = [
    'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
    'Gregory', 'john', 'kevin', 'Liam']
print(f"\nInitial list of players: {players}")

# All names Capitalized
all_caps: list[str] = [name.capitalize() for name in players]
print(f"New list with all names capitalized: {all_caps}")
# Only already capitalized names
capitalize_only: list[str] = [name for name in players if name[0].isupper()]
print(f"New list of capitalized names only: {capitalize_only}")
# Dictionary with random scores
scores: dict[str, int] = {name: random.randint(0, 1000) for name in all_caps}
print(f"\nScore dict: {scores}")
# Average Score
average: float = round(sum(scores.values()) / len(scores), 2)
print(f"Score average is {average}")
# High scores
high_scores: dict[str, int] = {
    name: score for name, score in scores.items() if score > average}
print(f"High scores: {high_scores}")
