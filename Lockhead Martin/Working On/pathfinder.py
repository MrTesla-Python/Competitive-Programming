def solve(grid, grid_l):
    if grid[0][0] == 0 or grid[-1][-1] == 0:
        return 0
    dp = [[0] * grid_l for _ in range(grid_l)]
    dp[0][0] = 1

    for i in range(grid_l):
        for j in range(grid_l):
            if grid[i][j] == 0:
                continue

            else:
                visited = set()
                visited.add((0,0))
                return unique_paths_dfs()

    return dp[-1][-1]
    
for t in range(int(input())):
    length = int(input())
    grid = [list(map(int, input().strip())) for _ in range(length)]
    print(solve(grid, length))