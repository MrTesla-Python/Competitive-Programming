from datetime import datetime
for t in range(int(input())):
    employee =  list(map(str, input().split(",")))
    hours = 0
    mins = 0
    for i in range(1, 6):
        time_obj = datetime.strptime(employee[i], "%H:%M")
        hours+=time_obj.hour
        mins+=time_obj.minute
    while mins >= 60:
        hours+=1
        mins-=60
    if mins == 0:
        if hours == 1:
            print(employee[0]+"="+str(hours)+" hour")
        else:
            print(employee[0]+"="+str(hours)+" hours")
    else:
        if hours == 1:
            if mins == 1:
                print(employee[0]+"="+str(hours)+" hour "+ str(mins) +" minute")
            else:
                print(employee[0]+"="+str(hours)+" hour "+ str(mins) +" minutes")
        else:
            if mins == 1:
                print(employee[0]+"="+str(hours)+" hours "+ str(mins) +" minute")
            else:
                print(employee[0]+"="+str(hours)+" hours "+ str(mins) +" minutes")