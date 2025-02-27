for t in range(int(input())):
    o, n = map(int, input().split())
    old_name = []*o
    old_phone = []*o
    old_address = []*o
    new_name = []*n
    new_phone = []*n
    new_address = []*n

    for i in range(o):
        name, phone, address = input().split(',')
        old_name.append(name)
        old_phone.append(phone)
        old_address.append(address)
    for i in range(n):
        name, phone, address = input().split(',')
        new_name.append(name)
        new_phone.append(phone)
        new_address.append(address)
    ans = []
    for index, name in enumerate(new_name):
        if name in old_name:
            old_index = old_name.index(name)
            if old_phone[old_index] != new_phone[index] and old_address[old_index] != new_address[index]:
                ans.append(name + " UPDATED BOTH")
            elif old_phone[old_index] != new_phone[index]:
                ans.append(name + " UPDATED PHONE NUMBER")
            elif old_address[old_index] != new_address[index]:
                ans.append(name + " UPDATED ADDRESS")
        if name not in old_name:
            ans.append(name + " CREATED")
    for index, name in enumerate(old_name):
        if name not in new_name:
            ans.append(name + " DELETED")
    for i in sorted(ans, key=str.lower):
        print(i)