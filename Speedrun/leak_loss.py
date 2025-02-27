import math
def round_half_up(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor
for t in range(int(input())):
    v, re, rl = map(float, input().split())
    print(f"{round_half_up(v/(re-rl) * rl):.0f}")