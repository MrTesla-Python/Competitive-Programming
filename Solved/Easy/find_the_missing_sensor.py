for t in range(int(input())):
    x = int(input())
    y = list(map(int, input().split()))
    list_x = [i for i in range(1,x+1)]
    for i in list_x:
        if i not in y:
            print(i)