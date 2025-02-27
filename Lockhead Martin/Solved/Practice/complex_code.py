for t in range(int(input())):

    L, C_limit, N_limit = map(int, input().strip().split())
    complexity = 1
    current_depth = 0
    max_depth = 0

    for i in range(L):
        line = input().strip()

        if line.startswith("If"):
            complexity += 1

        if line == "{":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        
        elif line == "}":
            current_depth -= 1
        

    status = "PASS" if (complexity <= C_limit and max_depth <= N_limit) else "FAIL"
    print(complexity, max_depth, status)