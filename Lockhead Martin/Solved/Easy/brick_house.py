for t in range(int(input())):
    small, large, length = map(int, input().split())
    while large and length >= 5:
        length-=5
        large-=1
    while small and length > 0:
        length-=1
        small-=1
    if length == 0:
        print("true")
    else:
        print("false")