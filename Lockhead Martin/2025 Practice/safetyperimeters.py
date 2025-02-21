import math
for t in range(int(input())):
    cords = int(input())
    x, y, safe = map(int, input().split())
    for i in range(cords):
        newx, newy = map(int, input().split())
        if safe > (math.sqrt(((newx - x) ** 2) + ((newy - y) **2))):
            print("("+str(newx)+","+str(newy)+") DANGER")

        else:
            print("("+str(newx)+","+str(newy)+") SAFE")