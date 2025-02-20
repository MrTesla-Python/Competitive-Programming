import math
def round_half_up(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor
for t in range(int(input())):
    v1, m1, v2, m2 = map(float, input().split(","))
    v = (m1*v1 + m2*v2)/(m1 + m2)
    print("%.2f" % round_half_up(v, 2))