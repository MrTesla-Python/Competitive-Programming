def binary_division(message, divisor="1011"):

    m = list(message)
    n = len(divisor) - 1

    for i in range(len(m) - n):
        if m[i] == "1":
            for j in range(n + 1):
                m[i + j] = str(int(m[i + j]) ^ int(divisor[j]))
    remained = "".join(m)
    return remained
for t in range(int(input())):
    data = input().strip()
    remainder = binary_division(data)
    final = binary_division(remainder)
    remainder = final[-3:]

    if remainder == "000":
        print("ok")

    else:
        print("corrupt")
        
