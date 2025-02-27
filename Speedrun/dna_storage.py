def binary_to_string(binary):
    binary_values = binary.split(' ')
    ascii_string = ''
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string

for t in range(int(input())):
    s = input()
    ans = []
    for i in range(0, len(s), 7):
        new = ""
        for j in range(7):
            if i + j < len(s):
                if s[i + j] == "A" or s[i + j] == "T":
                    new += '0'
                else:
                    new += '1'
        ans.append(new)
    binary_string = ' '.join(ans)
    print(binary_to_string(binary_string))