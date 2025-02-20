import math
def round_half_up(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor
for t in range(int(input())):
    w, n = map(float, input().split())
    area = (math.sqrt(3)/4)*w**2
    for _ in range(int(n)):
        area*=3/4
    print(str(int(3**n)) + " %.2f" % round_half_up(area, 2))