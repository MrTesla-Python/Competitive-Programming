for t in range(int(input())):
    R, C, B = map(int, input().strip().split())
    grid = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(B):
        x, y = map(int, input().strip().split())
        grid[x][y] = "*"
    
    vertices = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(R):
        for j in range(C):
            if grid[i][j] == "*":
                continue
            count = 0
            for di, dj in vertices:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    if grid[ni][nj] == "*":
                        count += 1
            grid[i][j] = count
    for i in range(R):
        print("".join(map(str, grid[i])).strip())