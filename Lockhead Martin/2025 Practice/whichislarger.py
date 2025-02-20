for i in range(int(input())):
    num_string = input().split()
    num_string.sort(key=lambda a: a * 10, reverse = True)

    if num_string[0] == "0":
        print(0)
    else:
        print("".join(num_string))