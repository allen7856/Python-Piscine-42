import sys


def analyze_scores() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"{arg} is not a valid score!")
            return

    total_players = len(scores)
    total_score: int = sum(scores)
    average: float = total_score / len(scores)
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = max(scores) - min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    analyze_scores()
