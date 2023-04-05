for t in range(int(input())):
    a, b = map(str, input().split())
    try:
        a = float(a)
    except:
        print("Invalid Dividend")
        continue
    try:
        b = float(b)
    except:
        print("Invalid Divisor")
        continue
    if float(b) == 0:
        print("Divide By Zero")
    else:
        print(round(a/b, 1))