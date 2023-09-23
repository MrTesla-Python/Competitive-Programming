import binascii
for t in range(int(input())):
    dna = input()
    binary_str = []
    binary = ""
    x = 1
    for i in dna:
        if x <= 7:
            if i.upper() == "A" or i.upper() == "T":
                binary += "0"
            else:
                binary += "1"
            x+=1
        else:
            binary_str.append(binary)
            binary = ""
            if i.upper() == "A" or i.upper() == "T":
                binary += "0"
            else:
                binary += "1"
            x = 2
    binary_str.append(binary)
    binary_str = [int(binary_str[i], 2) for i in range(len(binary_str))]
    print("".join(map(chr, binary_str)))
    