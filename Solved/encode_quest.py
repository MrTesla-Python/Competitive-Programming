T = int(input())
for _ in range(T):
    line = input().strip()
    keyword = input().strip()
    encrypt = ""
    spaces = 0
    for j in range(len(line)):
        if line[j] == ' ':
            spaces += 1
            encrypt += " "
            continue
        index = ord(line[j]) - ord('A')
        encode = chr(((ord(keyword[(j - spaces) % len(keyword)]) + index - ord('A')) % 26) + ord('A'))
        encrypt += encode
    print(encrypt)
