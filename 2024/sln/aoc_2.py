TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f"2024/test/test_{day}.txt" if TEST else f"2024/data/{day}.txt"

data = [list(map(int, i.split(" "))) for i in open(path, "r").read().splitlines()]


def is_safe(report):
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    return all(0 < abs(diff) < 4 for diff in diffs) and (
        report == sorted(report) or report == sorted(report)[::-1]
    )


def is_safe_2(report):
    return any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))


print(f"Answer to Part 1: {sum(is_safe(report) for report in data)}")
print(f"Answer to Part 2: {sum(is_safe_2(report) for report in data)}")
