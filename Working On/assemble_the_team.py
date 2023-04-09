for t in range(int(input())):
    people = input().split()
    people = [people[i].split("=") for i in range(len(people))]
    my_dict = {key: int(value) for key, value in people}
    ans = 0
    letters = ""
    for i in my_dict.keys():
        c = 0
        test_letters = i
        for j in my_dict.keys():
            if abs(my_dict[i] - my_dict[j]) <= 10:
                c+=1
                test_letters += j
        if c > ans:
            ans = c
            letters = test_letters
    print(letters)