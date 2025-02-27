def mult_poly(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result
for t in range(int(input())):
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    ans = ""
    for index, num in enumerate(mult_poly(p1, p2)):
        if num == 0:
            continue
        elif index == 0:
            ans += f"{num}"
        elif index == 1:
            if num == 1:
                ans += "+x"
            elif num == -1:
                ans += "-x"
            elif num > 1:
                ans += f"+{num}x"
            else:
                ans += f"-{num}x"
        else:
            if num < 0:
                ans += f"-{num}x^{index}"
            else:
                ans += f"+{num}x^{index}"
    if ans[0] == "+":
        ans = ans[1:]
    print(ans)