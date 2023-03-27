for t in range(int(input())):
    string = input()
    ans = ""
    for i in string:
        if i.isalnum() or i == " ":
            ans+=i
    print(ans)