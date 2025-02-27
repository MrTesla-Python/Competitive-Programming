for t in range(int(input())):
    cycles = int(input())
    cycles_chart = []
    for i in range(10):
        cycle = input()
        cycle = [i for i in cycle.strip()]
        cycles_chart.append(cycle)
    
    vertices = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for _ in range(cycles):
        new_chart = [cycle[:] for cycle in cycles_chart]
        for i in range(10):
            for j in range(10):
                count = 0
                for di, dj in vertices:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 10 and 0 <= nj < 10:
                        if cycles_chart[ni][nj] == "1":
                            count += 1
                if cycles_chart[i][j] == "1":
                    if count < 2 or count > 3:
                        new_chart[i][j] = "0"
                else:
                    if count == 3:
                        new_chart[i][j] = "1"
        cycles_chart = new_chart
    for i in range(10):
        print("".join(cycles_chart[i]).strip())
