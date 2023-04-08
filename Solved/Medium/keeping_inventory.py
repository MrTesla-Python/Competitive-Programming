def custom_sort(strings):
    weights = {
        '/': 0,
        '.': 1,
        '-': 2,
        'A': 3,
        'B': 4,
        'C': 5,
        'D': 6,
        'E': 7,
        'F': 8,
        'G': 9,
        'H': 10,
        'I': 11,
        'J': 12,
        'K': 13,
        'L': 14,
        'M': 15,
        'N': 16,
        'O': 17,
        'P': 18,
        'Q': 19,
        'R': 20,
        'S': 21,
        'T': 22,
        'U': 23,
        'V': 24,
        'W': 25,
        'X': 26,
        'Y': 27,
        'Z': 28,
        '0': 29,
        '1': 30,
        '2': 31,
        '3': 32,
        '4': 33,
        '5': 34,
        '6': 35,
        '7': 36,
        '8': 37,
        '9': 38,
    }
    weights['O'] = weights['0'] # Treat 'O' same as '0'
    return sorted(strings, key=lambda s: [weights.get(c, 999) for c in s])

for t in range(int(input())):
    strings = []
    for part in range(int(input())):
        strings.append(input())
    sorted_strings = custom_sort(strings)
    for i in sorted_strings:
        print(i)
