for t in range(int(input())):
    peoples = int(input())
    people = input()
    people = people.strip()[2:-2]
    people = people.split("],[")
    people = [part.split(',') for part in people]
    names, ages, instagrams, twitter, mobile, email = people
    p = []
    for i in range(peoples):
        p.append(input())
    dic = {}
    for i in range(len(p)):
        dic[names[i]] = (ages[i], instagrams[i], twitter[i], mobile[i], email[i])
    for i in p:
        print(f"Name: {i}")
        print(f"Age: {dic[i][0]}")
        print(f"Instagram: {dic[i][1]}")
        print(f"Twitter: {dic[i][2]}")
        print(f"Phone: {dic[i][3]}")
        print(f"Email: {dic[i][4]}")
