import math
def round_half_up(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor
for t in range(int(input())):
    cost = int(input())
    if cost >= 578251:
        ans = cost*.37
    elif cost >= 231251:
        ans = cost*.35
    elif cost >= 182101:
        ans = cost*.32
    elif cost >= 95376:
        ans = cost*.24
    elif cost >= 44727:
        ans = cost*.22
    elif cost >= 11001:
        ans = cost *.12
    else:
        ans = cost*.1
    print(int(round_half_up(ans)))