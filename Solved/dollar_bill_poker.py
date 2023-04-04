import re

t = int(input())
for i in range(t):
    s = input().strip()
    print(s, "=", end=" ")
    arr = sorted(list(s))
    s = "".join(arr)
    work = False
    test = [int(i) for i in s]
    test = set(test)
    test = list(test)
    test = "".join([str(elem) for elem in test])
    # Check FIVE OF A KIND
    for j in range(1, 10):
        if str(j)*5 in s:
            work = True
            print("FIVE OF A KIND")
            break
    if work:
        continue
    # Check FOUR OF A KIND
    for j in range(1, 10):
        if str(j)*4 in s:
            work = True
            print("FOUR OF A KIND")
            break
    if work:
        continue
    # Check FULL HOUSE
    for j in range(1, 10):
        for k in range(1, 10):
            if j != k and (str(j)*2 in s and str(k)*3 in s or str(k)*2 in s and str(j)*3 in s):
                work = True
                print("FULL HOUSE")
                break
        if work:
            break
    if work:
        continue
    # Check STRAIGHT
    for j in range(1, 6):
        if re.search(str(j)+str(j+1)+str(j+2)+str(j+3)+str(j+4), test):
            work = True
            print("STRAIGHT")
            break
    if work:
        continue
    # Check THREE OF A KIND
    for j in range(1, 10):
        if str(j)*3 in s:
            work = True
            print("THREE OF A KIND")
            break
    if work:
        continue
    # Check TWO PAIR
    for j in range(1, 10):
        for k in range(1, 10):
            if j != k and str(j)*2 in s and str(k)*2 in s:
                work = True
                print("TWO PAIR")
                break
        if work:
            break
    if work:
        continue
    # Check PAIR
    for j in range(1, 10):
        if str(j)*2 in s:
            work = True
            print("PAIR")
            break
    if work:
        continue
    print(s[-1])
