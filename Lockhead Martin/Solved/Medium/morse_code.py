for t in range(int(input())):
    morse_code = {}
    reverse = {}
    for i in range(26):
        key, val = map(str, input().split(" ", 1))
        morse_code[key] = val
        reverse[val] = key
    decode = input()
    code = input()
    decode_s = ""
    code_s = ""
    for i in decode:
        if i in morse_code.keys():
            decode_s += morse_code[i]
            decode_s+="   "
        else:
            decode_s+="    "
    print(decode_s.strip())
    code = code.split("   ")
    for i in range(len(code)):
        code[i] = code[i].strip()
    for i in range(len(code)):
        if code[i] in reverse:
            code_s += reverse[code[i]]
        else:
            code_s+=" "
    print(code_s.strip())