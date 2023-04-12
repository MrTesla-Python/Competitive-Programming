for t in range(int(input())):
    denominations = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.25, 0.10, 0.05, 0.01]
    change_due = float(input())
    change_dict = {}
    
    for denomination in denominations:
        count = round(int(change_due / denomination), 1)
        if count >= 0:
            change_dict[denomination] = count
            change_due -= round((count * denomination), 2)
            change_due = round(change_due, 2)
    list1 = [str(i) for i in change_dict.values()]
    print("".join(list1))