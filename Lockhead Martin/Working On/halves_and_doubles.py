for t in range(int(input())):
    first, second = map(float, input().strip().split())
    ans = 0
    if first % 2 == 0:
        print(f"{int(first)} {int(second)} ***")
    else:
        print(f"{int(first)} {int(second)}")
        ans += second
    while first > 1:
        new = first // 2
        second = second * 2
        if new % 2 == 0 and first/2 != new:
            print(f"{int(new)}* {int(second)} ***")
        elif new % 2 == 0:
            print(f"{int(new)} {int(second)} ***")
        elif first/2 != new:
            print(f"{int(new)}* {int(second)}")
            ans += second
        else:
            print(f"{int(new)} {int(second)}")
            ans += second
        first = new
    print(int(ans))
