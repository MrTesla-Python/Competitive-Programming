import decimal

def round_to_nearest_decimal(number):
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    return    float(decimal.Decimal(str(number)).quantize(decimal.Decimal('.1')))
for t in range(int(input())):
    people, answers = input().split()
    people = int(people)
    for i in range(people):
        c = 0
        person, person_answers = input().split()
        for question, answer in enumerate(person_answers):
            if answer != answers[question]:
                c+=1
        answer = (len(answers)-c)/len(answers)*100
        answer = round_to_nearest_decimal(answer)
        answer = answer/100
        if answer >= .9:
            print(person, "{:.1%}".format(answer), "A")
        elif answer >= .8:
            print(person, "{:.1%}".format(answer), "B")
        elif answer >= .7:
            print(person, "{:.1%}".format(answer), "C")
        elif answer >= .6:
            print(person, "{:.1%}".format(answer), "D")
        else:
            print(person, "{:.1%}".format(answer), "F")