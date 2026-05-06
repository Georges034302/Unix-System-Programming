#!/usr/bin/env python3
"""
Simple player registration and scoreboard simulator.
Usage: python3 game_dictionary.py
"""

import random

def read_int(prompt, minimum, maximum):
    value = int(input(prompt))
    # Enforce an inclusive range for menu-driven numeric input.
    if not minimum <= value <= maximum:
        raise ValueError(f"Enter a value between {minimum} and {maximum}.")
    return value


def register_players(n):
    # Generate unique player IDs so each player has a distinct record key.
    ids = random.sample(range(1, 100), n)
    return [
        {
            "id": pid,
            "name": f"Player_{pid:02d}",
            "score": 0,
        }
        for pid in ids
    ]


def show_scoreboard(players, title):
    print(f"\n{title}")
    print("ID  Name        Score")
    print("--  ----------  -----")

    for player in players:
        print(f"{player['id']:02d}  {player['name']:<10}  {player['score']:>5}")


def sort_by_top_score(players):
    # Highest scores first for "top players" display.
    return sorted(players, key=lambda player: player["score"], reverse=True)


def generate_scores(players):
    for player in players:
        # Simulate one game result per player.
        player["score"] = random.randint(1, 100)


def handle_register():
    n = read_int("How many players (1-99): ", 1, 99)
    players = register_players(n)
    print(f"Registered {len(players)} players.")
    return players


def handle_play(players):
    generate_scores(players)
    print("Scores generated.")


def handle_show(players):
    show_scoreboard(players, "Scoreboard (All Players)")


def handle_top(players):
    m = read_int(f"How many top players to show (1-{len(players)}): ", 1, len(players))
    top_players = sort_by_top_score(players)[:m]
    show_scoreboard(top_players, f"Top {m} Players")

def main():
    players = []
    choice = ""

    # Keep running until the user chooses exit.
    while choice != "x":
        print("\nOptions: r=register  p=play  s=show  t=top m  x=exit")
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
