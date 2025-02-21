for t in range(int(input())):
    parts = int(input())
    og, s, w, p, c = map(float, input().split())
    best_model = og
    ans = s+w+p+c
    realans = s+w+p+c
    for t in range(parts):
        part, s1, w1, p1, c1 = map(float, input().split())
        if ans * 0.8 > (s1 + w1 + p1 + c1):
            if realans > s1+w1+p1+c1:
                realans = min(realans, s1+w1+p1+c1)
                best_model = part
    print(str(int(best_model)) + " " + str(int(realans)))