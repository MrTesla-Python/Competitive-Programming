for t in range(int(input())):
    R, C = map(int, input().split())
    test = []
    for i in range(R):
        test.append(input().split(","))
    ans = [[0 for j in range(R)] for i in range(C)]
    for i in range(R):
        for j in range(C):
            ans[j][i] = test[i][j]
            
    for i in range(len(ans)):
        print(",".join(ans[i]))