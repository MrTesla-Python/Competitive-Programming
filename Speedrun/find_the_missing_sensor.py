for t in range(int(input())):
    t = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if s[0] != 1:
        print(1)
    elif s[-1] != t:
        print(t)
    else:
        for i in range(len(s) - 1):
            if s[i] + 1 != s[i+1]:
                print(s[i] + 1)
                break