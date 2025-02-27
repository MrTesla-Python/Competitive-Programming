from collections import Counter
for t in range(int(input())):
    x, y = map(int, input().split())
    x += y
    c = []
    for t in range(x):
        s = input()
        c.append(s.strip())
    count = Counter(c)
    ans = []
    for c in count:
        if count[c] == 1:
            ans.append(c)
    ans.sort(key=str.lower)
    for a in ans:
        print(a.strip())