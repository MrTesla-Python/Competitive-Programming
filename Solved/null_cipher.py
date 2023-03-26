for t in range(int(input())):
    vowels  = [i for i in "aeiou"]
    s = input()
    left = 0
    ans = ""
    while left < len(s):
        if s[left] in vowels:
            ans+=s[left+1]
            left+=1
        left+=1
    print(ans)