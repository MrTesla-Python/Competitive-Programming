from collections import Counter
for t in range(int(input())):
    texts = input().split()
    text = "".join(texts)
    print(max(Counter(text).values()))