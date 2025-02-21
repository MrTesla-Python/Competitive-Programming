from collections import Counter
def get_letter_score(letter):
    for key, value in points.items():
        if letter in key:
            return value
for t in range(int(input())):
    points = {
    ("A", "E", "I", "L", "N", "O", "R", "S", "T", "U"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4, 
    ("K",): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}
    string = input().strip()
    ans = 0
    for i in string:
        print(str(i) + "=" + str(get_letter_score(i)))
        ans += get_letter_score(i)
    print("TOTAL="+str(ans))

