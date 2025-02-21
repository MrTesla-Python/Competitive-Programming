import re
for t in range(int(input())):
    lines = int(input())
    reference_text = [input() for line in range(lines)]
    keyword = input()
    reference_text = " ".join(reference_text)
    #print(reference_text)

    sentences = re.split(r"([.!?])", reference_text)
    sentences = ["".join(sentences[i:i+2]).strip() for i in range(0, len(sentences)-1, 2)]

    #print(sentences)

    results = []

    for sentence in sentences:
        words = sentence.split()
        lower = (w.lower().strip(",.!?") for w in words)

        for i, word in enumerate(lower):
            if word == keyword:
                start = max(0, i-3)
                end = min(len(words), i + 6)
                if (end < len(words) and start > 0):
                    context = words[start:end]
                    context[i - start] = f"*{words[i]}*"
                    results.append("..."+" ".join(context) + "...")
                elif end < (len(words)):
                    context = words[start:end]
                    context[i - start] = f"*{words[i]}*"
                    results.append(" ".join(context)+"...")
                elif start > 0:
                    context = words[start:end]
                    context[i - start] = f"*{words[i]}*"
                    results.append("..."+" ".join(context))
                else:
                    context = words[start:end]
                    context[i - start] = f"*{words[i]}*"
                    results.append(" ".join(context))
    for res in results:
        print(res.strip())
