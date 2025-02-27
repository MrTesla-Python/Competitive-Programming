import math
for t in range(int(input())):

    asteroids = int(input())
    asteroids_d = {}
    for i in range(asteroids):
        x, y = map(int, input().strip().split())
        d = math.sqrt(x**2 + y**2)
        asteroids_d[d] = (x, y)
    for dist, cords in sorted(asteroids_d.items()):
        print(cords[0], cords[1])
    