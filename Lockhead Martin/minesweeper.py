for t in range(int(input())):
    R, C, B = map(int, input().split())
    mine_map = [[0 for j in range(C)] for i in range(R)]
    for i in range(B):
        x, y = map(int, input().split())
        mine_map[x][y] = "*"
    vertices = [(-1, 0),(1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for i in range(R):
        for j in range(C):
            if mine_map[i][j] == "*":
                continue
            count = 0
            for vertex in vertices:
                x, y = vertex
                if 0 <= i + x < R and 0 <= j + y < C and mine_map[i + x][j + y] == "*":
                    count += 1
            mine_map[i][j] = count
    print(mine_map)
    for i in range(R):
        print("".join(map(str, mine_map[i])))