import math
def round_half_up(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor
for t in range(int(input())):
    words = input().split()
    dates = input().split()
    dates = [float(i) for i in dates]

    string = "abcdefghijklmnopqrstuvwxyz"
    Hn = 0
    for i in range(10):
        points = 0
        for char in words[i]:
            points += string.index(char)+1
        Hn = ((dates[i] + points + i + 1 + Hn) * 50) / 147

    print(int((round_half_up(Hn))))