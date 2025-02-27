for t in range(int(input())):
    r, c = map(int, input().strip().split())
    grid = [[0 for _ in range(c)] for _ in range(r)]
    bools = [[False for _ in range(c)] for _ in range(r)]
    for i in range(r):
        row_data = input().strip().split()
        for j in range(c):
            cell = row_data[j]
            bools[i][j] = True if cell[-1] == "L" else False
            grid[i][j] = int(cell[:-1])
    answers = []
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(r):
        for j in range(c):
            if bools[i][j]:
                valid = True
                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        if grid[ni][nj] < grid[i][j]:
                            valid = False
                            break
                if valid:
                    answers.append((grid[i][j], (i, j)))
    print(answers[1][0])
    answers = sorted(answers, key=lambda x: (x[0], x[1][0], x[1][1]))
    for answer in answers:
        print(answer[0], answer[1][0], answer[1][1])