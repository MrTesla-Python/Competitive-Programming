def solve(grid, i, j, visited):
    result = 0

    if (i, j) == (len(grid) - 1, len(grid) - 1):
        return 1
    if (i - 1, j) in visited:
        visited.remove((i - 1, j))
        result += solve(grid, i - 1, j, visited)
        visited.add((i - 1, j))

    if (i + 1, j) in visited:
        visited.remove((i + 1, j))
        result += solve(grid, i + 1, j, visited)
        visited.add((i + 1, j))
    
    if (i, j - 1) in visited:
        visited.remove((i, j - 1))
        result += solve(grid, i, j - 1, visited)
        visited.add((i, j - 1))
    
    if (i, j + 1) in visited:
        visited.remove((i, j + 1))
        result += solve(grid, i, j + 1, visited)
        visited.add((i, j + 1))
    
    return result
    
for t in range(int(input())):
    length = int(input())
    grid = [list(map(int, input().strip())) for _ in range(length)]
    if grid[0][0] == 0 or grid[-1][-1] == 0:
        print(0)
    else:
        visited = set()
        for i in range(length):
            for j in range(length):
                if grid[i][j] == 1:
                    visited.add((i, j))
        visited.remove((0, 0))
        print(solve(grid, 0, 0 , visited))
        
   