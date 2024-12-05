from collections import defaultdict

TEST = 0
day = __file__.split("\\")[-1][:-3]

path = f'2024/test/test_{day}.txt' if TEST else f'2024/data/{day}.txt'

rules, updates = [i.split('\n') for i in open(path, 'r').read().split('\n\n')]

d = defaultdict(list)
for rule in rules:
    a, b = rule.split("|")
    d[a].append(b)


def fix_page(page):
    pos = 0
    while pos < len(page) - 1:
        last_pos = pos
        for i in range(pos + 1, len(page)):
            if page[pos] in d[page[i]]:
                last_pos = i
        if last_pos != pos:
            page.insert(last_pos, page.pop(pos))
        else:
            pos += 1
    return int(page[len(page) // 2])


cnt = 0
cnt2 = 0
for pages in [p.split(',') for p in updates]:
    correct = True
    for v in pages:
        if any(i in pages and pages.index(i) < pages.index(v) for i in d[v]):
            correct = False
    if correct:
        cnt += int(pages[len(pages) // 2])
    else:
        cnt2 += fix_page(pages)

print(f"Answer to Part 1: {cnt}")
print(f"Answer to Part 2: {cnt2}")
