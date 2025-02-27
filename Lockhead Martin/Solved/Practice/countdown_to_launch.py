import math
for t in range(int(input())):
    check = False
    times = int(input())
    for time in range(times):
        n = input().split()
        clouds = int(n[2])
        speed = float(n[3])
        degree = int(n[4])
        ns = math.cos(math.radians(degree)) * speed
        ew = math.sin(math.radians(degree)) * speed

        if abs(ns) < 20 and abs(ew) < 40 and clouds < 1000 and check == False:
            print(" ".join(n[0:2]))
            check = True
    if not check:
        print("ABORT LAUNCH")
