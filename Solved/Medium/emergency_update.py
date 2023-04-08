for t in range(int(input())):
    old_n, new_n = map(int, input().split())
    ans = []
    old_people = old_n*[0]
    old_phone = old_n*[0]
    old_addy = old_n*[0]
    new_people = new_n*[0]
    new_phone = new_n*[0]
    new_addy = new_n*[0]
    for i in range(old_n):
        people, phone, addy = input().split(',')
        old_people[i] = people
        old_phone[i] = phone
        old_addy[i] = addy
    for i in range(new_n):
        people, phone, addy = input().split(',')
        new_people[i] = people
        new_phone[i] = phone
        new_addy[i] = addy
    for pos, person in enumerate(new_people):
        if person in old_people:
            index = old_people.index(person)
            if old_phone[index] != new_phone[pos] and old_addy[index] != new_addy[pos]:
                ans.append(person + " UPDATED BOTH")
            elif old_phone[index] != new_phone[pos]:
                ans.append(person + " UPDATED PHONE NUMBER")
            elif old_addy[index] != new_addy[pos]:
                ans.append(person + " UPDATED ADDRESS")
        if person not in old_people:
            ans.append(person + " CREATED")
    for pos, person in enumerate(old_people):
        if person not in new_people:
            ans.append(person + " DELETED")
    for i in sorted(ans, key=str.lower):
        print(i)