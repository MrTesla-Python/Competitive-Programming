from collections import defaultdict
import sys
for _ in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    t = x + y
    m = defaultdict(int)
    for _ in range(t):
        s = sys.stdin.readline()
        m[s] += 1
    st = set()
    for k, v in m.items():
        if v == 1:
            st.add(k)
    for x in sorted(st):
        print(x)
