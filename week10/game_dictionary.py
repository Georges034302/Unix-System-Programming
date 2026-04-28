#!/usr/bin/env python3
import random

# Reads one integer from user input within a given range.
def read_int(prompt, minimum, maximum):
    value = int(input(prompt))

    if not minimum <= value <= maximum:
        raise ValueError(f"Enter a value between {minimum} and {maximum}.")

    return value


# Registers n players using unique IDs from random.sample(range(1, 100), n).
def register_players(n):
    ids = random.sample(range(1, 100), n)
    players = []

    for pid in ids:
        players.append({
            "id": pid,
            "name": f"Player_{pid:02d}",
            "score": 0,
        })

    return players


# Shows a scoreboard table for the given player list.
def show_scoreboard(players, title):
    print(f"\n{title}")
    print("ID  Name        Score")
    print("--  ----------  -----")

    for player in players:
        print(f"{player['id']:02d}  {player['name']:<10}  {player['score']:>5}")


# Returns the score value for one player record.
def get_score(player):
    return player["score"]


# Returns players sorted by score from highest to lowest.
def sort_by_top_score(players):
    return sorted(players, key=get_score, reverse=True)


# Generates scores for all registered players.
def generate_scores(players):
    for player in players:
        player["score"] = random.randint(1, 100)


# Handles menu choice 'r': register players and show scoreboard.
def handle_register():
    n = read_int("How many players (1-99): ", 1, 99)
    players = register_players(n)
    print(f"Registered {len(players)} players.")
    return players


# Handles menu choice 'p': generate scores for all players.
def handle_play(players):
    generate_scores(players)
    print("Scores generated.")


# Handles menu choice 's': show full scoreboard.
def handle_show(players):
    show_scoreboard(players, "Scoreboard (All Players)")


# Handles menu choice 't': show top-m players by score.
def handle_top(players):
    m = read_int(f"How many top players to show (1-{len(players)}): ", 1, len(players))
    top_players = sort_by_top_score(players)[:m]
    show_scoreboard(top_players, f"Top {m} Players")

# Runs a simple menu: r=register, p=generate scores, s=show, t=top m, x=exit.
def main():
    players = []
    choice = ""

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
