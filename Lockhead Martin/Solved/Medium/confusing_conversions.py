for t in range(int(input())):
    x = list(map(str, input().split()))
    if x[0] == "formatHeight":
        print(str(x[1])+"'"+str(x[2])+'"')
    elif x[0] == "formatDate":
        year =  x[1]
        month = x[2]
        day = x[3]
        if int(month) < 10:
            month = "0"+month
        if int(day) < 10:
            day = "0"+day
        print(year+month+day)
    elif x[0] == "concatenate":
        ans = ""
        for i in range(1, len(x)):
            if i == len(x)-1:
                ans+=x[i]
            else:
                ans+=x[i]+","
        print(ans)