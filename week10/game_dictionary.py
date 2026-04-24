#!/usr/bin/env python3
import random

def create_game(size):
    game = {}
    used_ids = set()

    while len(game) < size:
        pid = random.randint(100, 999)

        if pid in used_ids:
            continue

        used_ids.add(pid)
        game[pid] = {
            "name": f"Player_{random.randint(10, 99)}",
            "score": random.randint(1, 100)
        }

    return game

def sort_by_score(game):
    items = list(game.items())

    def score_key(item):
        return item[1]["score"]

    items.sort(key=score_key, reverse=True)
    return items

def show(game, sort_scores=False):
    items = sort_by_score(game) if sort_scores else list(game.items())

    if not items:
        print("No players loaded.")
        return

    for pid, data in items:
        print(f"{pid} - {data['name']} (Score: {data['score']})")

def main():
    game = {}

    while True:
        print("\nOptions: c=create  s=sort  r=raw  x=exit")
        choice = input("Choice: ").strip().lower()

        match choice:
            case "c":
                try:
                    size = int(input("Add players: "))
                    game = create_game(size)
                    show(game)
                except ValueError:
                    print("Enter a valid integer.")
            case "s":
                show(game, True)
            case "r":
                show(game)
            case "x":
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
