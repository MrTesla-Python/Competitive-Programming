for t in range(int(input())):
    s = input()
    ans = []
    for i in s:
        if i.isalpha() or i in "1234567890 ":
            ans.append(i)
    print("".join(ans))