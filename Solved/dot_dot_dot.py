for t in range(int(input())):
    dict = {y:x+1 for x,y in enumerate("abcdefghijklmnopqrstuvwxyz")}
    ans =  0
    x = input()
    for i in x:
        ans+=dict[i]
    print(ans)