def find_start(grid, word):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == word[0]:
                if dfs(grid, word, i, j, 0):
                    return True
def dfs(grid, word, i, j, idx):
    if idx == len(word):
        return True
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != word[idx]:
        return False
    if grid[i][j] == word[idx]:
        found = dfs(grid, word, i+1, j, idx+1) or dfs(grid, word, i-1, j, idx+1) or dfs(grid, word, i, j+1, idx+1) or dfs(grid, word, i, j-1, idx+1) or dfs(grid, word, i+1, j+1, idx+1) or dfs(grid, word, i-1, j-1, idx+1) or dfs(grid, word, i-1, j+1, idx+1) or dfs(grid, word, i+1, j-1, idx+1)
    else:
        return False
    return found
for t in range(int(input())):
    R, C = map(int, input().split())
    grid = [list(input().split()) for _ in range(R)]
    
    
    words = int(input())
    word_list = [input().strip() for _ in range(words)]

    for word in word_list:
        if find_start(grid, word.strip()):
            print(word.strip())

    