import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argv = sys.argv
    argc = len(argv)
    j = 0
    i = 1
    while i < argc:
        try:
            int(argv[i])
            j += 1
        except Exception:
            print(f"Invalid parameter: '{argv[i]}'")
        i += 1
    if j == 0:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
    else:
        arr = [0] * j
        k = 0
        i = 0
        while i < argc:
            try:
                arr[k] = int(argv[i])
                k += 1
                i += 1
            except Exception:
                i += 1
        s = sum(arr)
        total = argc - 1
        avg = s / total
        high = max(arr)
        low = min(arr)
        score = high - low
        print(f"Scores processed: {arr}")
        print(f"Total players: {j}")
        print(f"Total score: {s}")
        print(f"Average score: {avg}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {score}")


if __name__ == "__main__":
    main()
