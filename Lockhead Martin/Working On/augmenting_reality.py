import math
for t in range(int(input())):
    R, W, H = map(float, input().strip().split())
    for i in range(int(W+1)):
        for j in range(int(H+1)):
            if (i)**2 + (j)**2 > R**2:
                print(str(int(i)) + "," + str(int(j)))