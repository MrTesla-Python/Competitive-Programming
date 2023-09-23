def calc(x):
    factors = []
    for n in range(1, x):
        if x % n == 0:
            factors.append(n)
    return factors

def get_large(x):
    return calc(x)[-1] #return the last factor in the list
def sum_digits2(n):
    s = 0
    while n:
        n, remainder = divmod(n, 10)
        s += remainder
    return s
    
def encode_lower(letter):
    letter_to_number = {}
    number_to_letter = {}
    for i in range(26):
        letter_to_number[chr(ord('a') + i)] = i + 1
    for i in range(1, 27):
        number_to_letter[i] = chr(ord('a') + i - 1)
    if letter in "abcde":
        number = letter_to_number[letter]
        number = number + 6
        ans =  number_to_letter[number]
        
    elif letter in "fghij":
        number = letter_to_number[letter]
        number = number**2
        if number > 26:
            number =  number%26
        ans = number_to_letter[number]

    elif letter in "klmno":
        number = letter_to_number[letter]
        number =  number%3
        number = number*5
        number += 1
        if number > 26:
            number =  number%26
        ans = number_to_letter[number]
    elif letter in "pqrst":
        number = letter_to_number[letter]
        number = sum_digits2(number)
        number = number * 8
        if number > 26:
            number =  number%26
        ans = number_to_letter[number]
    elif letter in "uvwxyz":
        number = letter_to_number[letter]
        number = get_large(number)
        number = number * 2
        if number > 26:
            number =  number%26
        ans = number_to_letter[number]
    return ans

for t in range(int(input())):
    string = input()
    string = string.lower()
    ans = ""
    for i in string:
        new = encode_lower(i)
        ans += new
    print(ans.upper())