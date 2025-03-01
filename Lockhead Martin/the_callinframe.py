for t in range(int(input())):
    string = input().strip()
    no = True
    for i in string:
        if not i.isalpha():
            no = False
            break
    grid = []
    if not no or len(string) < 5 or len(string) > 32:
        print("Not a Calliframe")
    else:
        grid = [[" " for _ in range(len(string))] for _ in range(len(string))]
        for i in range(len(string)):
            grid[i][0] = string[i]
        for index, num in enumerate(reversed(string)):
            grid[index][-1] = num
        for i in range(len(string)):
            grid[0][i] = string[i]
        for index, num in enumerate(reversed(string)):
            grid[-1][index] = num
        for i in range(len(string)):
            print("".join(grid[i]))