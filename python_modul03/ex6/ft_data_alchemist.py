import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    new_list = [i.capitalize() for i in players]
    print(f"New list with all names capitalized: {new_list}")

    new_list2 = [i for i in players if i == i.capitalize()]
    print(f"New list of capitalized names only: {new_list2}")

    scores = {i: random.randint(1, 1000) for i in new_list}
    print(f"Score dict: {scores}")

    avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    high_scores = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
