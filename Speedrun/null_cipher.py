for t in range(int(input())):
    s = input()
    ans = ""
    left = 0
    while left < len(s):
        if s[left] in "aeiou":
            ans+=s[left+1]
            left+=1
        left+=1 
    print(ans)