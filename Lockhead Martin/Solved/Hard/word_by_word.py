import statistics
import decimal
from collections import Counter

def round_to_nearest_decimal(number):
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    return float(decimal.Decimal(str(number)).quantize(decimal.Decimal('.1')))

def get_words(words):
    ans = []
    words_all_letters = ""
    for i in words:
        if i.isalpha():
            words_all_letters += i
        elif i == " ":
            words_all_letters += i
    ans = words_all_letters.split()
    return ans

for t in range(int(input())):
    word_list = []
    lengths = []
    sents = int(input())
    for n in range(sents):
        for i in get_words(input()):
            word_list.append(i)
    for i in word_list:
        lengths.append(len(i))
    
    sorted_lengths = sorted(lengths)
    range_val = sorted_lengths[-1]-sorted_lengths[0]
    mean = statistics.mean(lengths)
    median = statistics.median(lengths)
    modes = statistics.multimode(lengths)
    modes = sorted(modes)
    modes = [str(i) for i in modes]
    
    print("Average: " + str(round_to_nearest_decimal(mean)))
    print("Median: " + str(round_to_nearest_decimal(median)))
    print("Modes: " + ",".join(modes))
    print("Range: " + str(range_val))

    count = Counter(lengths)

    num = sorted_lengths[0]
    while num <= sorted_lengths[-1]:
        if num < 10:
            ans = " " + str(num) +"|"
        else:
            ans = str(num) + "|"
        if num in count.keys():
            ans += "x"*count[num]
            
        print(ans)
        num += 1