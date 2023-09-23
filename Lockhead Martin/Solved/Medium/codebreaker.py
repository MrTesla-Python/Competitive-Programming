import decimal
def round_to_nearest_decimal(number):
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    return    float(decimal.Decimal(str(number)).quantize(decimal.Decimal('.01')))
from collections import Counter
for t in range(int(input())):
    sents = []
    sentence = ""
    letters = ""
    for i in range(int(input())):
        sents.append(input())
    for i in sents:
        sentence += i
    sentence = sentence.upper()
    for i in sentence:
        if i.isalpha():
            letters+=i
    counts = Counter(letters)
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        percent = (counts[i]/len(letters))*100
        percent = round_to_nearest_decimal(percent)
        print(i + ": " + str("{:.2f}".format(percent)) + "%")