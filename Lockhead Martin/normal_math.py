def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
import math
for t in range(int(input())):
    R, C = map(int, input().split())
    grid = [list(float(t) for t in input().split()) for _ in range(R)]
    ans = 0
    for i in range(R):
        for j in range(C):
            ans += grid[i][j]**2

    print(f"{round(math.sqrt(ans), 2):.2f}")