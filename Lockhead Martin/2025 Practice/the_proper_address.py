for t in range(int(input())):
    ip = input().split(".")
    x = True
    if (len(ip) != 4):
        x = False
    else:
        for i in ip:
            if not i.isdigit() or int(i) > 255 or int(i) < 0 or (int(i) < 0):
                x = False
                break

    print("VALID" if x else "INVALID")
            