

import sys

def count_of_args(av: str) -> None:
    if len(av) <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    valid_scores = []
    for arg in av[1:]:
        try:
            num = int(arg)
            valid_scores.append(num)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not valid_scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    else:
        print(f"Scores processed: {valid_scores}")
        print(f"Total players: {len(av) - 1}")
        print(f"Total score: {sum(valid_scores)}")
        average = sum(valid_scores) / (len(av) - 1)
        print(f"Average score: {int(average)}")
        print(f"High score: {max(valid_scores)}")
        print(f"Low score: {min(valid_scores)}")
        ranges = max(valid_scores) - min(valid_scores)
        print(f"Score range: {int(ranges)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    count_of_args(sys.argv)
