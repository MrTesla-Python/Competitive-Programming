from collections import Counter
for t in range(int(input())):
    counts = {}
    for address in range (int(input())):
        normal, mac = input().strip().split()
        if normal not in counts:
            counts[normal] = set()
        counts[normal].add(mac)
    for i in sorted(counts, key=lambda x: list(map(int, x.split(".")))):
        print(f"{i} {len(counts[i])}")