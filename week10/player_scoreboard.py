#!/usr/bin/env python3
"""
Register players, generate game scores, and view the scoreboard.
Usage:
    python3 player_scoreboard.py
    Choose r to register players, p to generate scores, s to show all scores,
    or t to show the top three players. Choose x to exit.
"""

import random

# Register players with unique IDs and zero scores.
def handle_register():
    n = int(input("How many players (1-99): "))
    if not 1 <= n <= 99:
        raise ValueError("Enter a value between 1 and 99.")

    player_ids = random.sample(range(1, 100), n)
    players = [
        {"id": player_id, "name": f"Player_{player_id:02d}", "score": 0}
        for player_id in player_ids
    ]
    print(f"Registered {len(players)} players.")
    return players

# Generate a random score for each player.
def handle_play(players):
    for player in players:
        player["score"] = random.randint(1, 100)
    print("Scores generated.")

# Display the full scoreboard.
def handle_show(players):
    print("\nScoreboard (All Players)")
    print("ID  Name        Score")
    print("--  ----------  -----")
    for player in players:
        print(f"{player['id']:02d}  {player['name']:<10}  {player['score']:>5}")

# Display the three highest-scoring players.
def handle_top(players):
    top_players = sorted(
        players, key=lambda player: player["score"], reverse=True
    )[:3]
    print("\nTop 3 Players")
    print("ID  Name        Score")
    print("--  ----------  -----")
    for player in top_players:
        print(f"{player['id']:02d}  {player['name']:<10}  {player['score']:>5}")

# Run the player registration, scoring, and scoreboard menu.
def main():
    players = []
    choice = ""

    # Keep running until the user chooses exit.
    while choice != "x":
        print("\nr - register players")
        print("p - play and generate scores")
        print("s - show scoreboard")
        print("t - show top 3")
        print("x - exit")
        choice = input("Choice: ").strip().lower()

        if choice == "r":
            players = handle_register()

        elif choice == "p":
            handle_play(players)

        elif choice == "s":
            handle_show(players)

        elif choice == "t":
            handle_top(players)

        elif choice == "x":
            print("Exiting...Bye!")

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
