#!/usr/bin/env python3

def demonstrate_comprehensions() -> None:
    players: list[dict] = [
            {"name": "alice", "score": 2300, "status": "active",
                "region": "north",
                "achievements": ["first_kill", "level_10", "boss_slayer",
                                 "speed_demon", "collector"]},
            {"name": "bob", "score": 1800, "status": "active",
                "region": "east",
                "achievements": ["first_kill", "level_10", "treasure_hunter"]},
            {"name": "charlie", "score": 2150, "status": "active",
                "region": "central",
                "achievements": ["first_kill", "level_10", "boss_slayer",
                                 "speed_demon", "collector", "explorer"]},
            {"name": "diana", "score": 2050, "status": "inactive",
                "region": "north",
                "achievements": ["first_kill", "level_10", "boss_slayer",
                                 "legend"]},
            {"name": "eve", "score": 950, "status": "inactive",
                "region": "east", "achievements": ["first_kill"]},
            {"name": "frank", "score": 1400, "status": "inactive",
                "region": "central",
                "achievements": ["first_kill", "level_10"]},
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers: list[str] = [p["name"] for p in players
                               if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled: list[int] = [p["score"] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players: list[str] = [p["name"] for p in players
                                 if p["status"] == "active"]
    print(f"Active players: {active_players}")

    top_active: list[tuple] = [(p["name"], p["score"]) for p in players
                               if p["status"] == "active"
                               and p["score"] > 2000]
    print(f"Top active players: {top_active}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores: dict[str, int] = {p["name"]: p["score"] for p in players
                                     if p["status"] == "active"}
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
            "high": len([p for p in players if p["score"] >= 2000]),
            "medium": len([p for p in players
                           if 1500 <= p["score"] < 2000]),
            "low": len([p for p in players if p["score"] < 1500]),
            }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {p["name"]: len(p["achievements"])
                                          for p in players
                                          if p["status"] == "active"}
    print(f"Achievement counts: {achievement_counts}")

    last_achievement: dict[str, str] = {p["name"]: p["achievements"][-1]
                                        for p in players}
    print(f"Player's last achievement: {last_achievement}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set[str] = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements: set[str] = {a for p in players
                                     for a in p["achievements"]
                                     if p["score"] > 2000}
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set[str] = {p["region"] for p in players
                                if p["status"] == "active"}
    print(f"Active regions: {active_regions}")

    inactive_achievements: set[str] = {a for p in players
                                       for a in p["achievements"]
                                       if p["status"] == "inactive"}
    print(f"Achievements held by inactive players: "
          f"{inactive_achievements}")

    print("\n=== Combined Analysis ===")

    scores: list[int] = [p["score"] for p in players]
    all_achievements: set[str] = {a for p in players
                                  for a in p["achievements"]}
    top: dict = sorted(players, key=lambda p: p["score"])[-1]

    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"Top performer: {top['name']} ({top['score']} points, "
          f"{len(top['achievements'])} achievements)")


if __name__ == "__main__":
    demonstrate_comprehensions()
