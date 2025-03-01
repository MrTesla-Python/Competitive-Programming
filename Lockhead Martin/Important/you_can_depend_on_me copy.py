def compute_level(node, dependencies, memo):
    if node in memo:
        return memo[node]
    if node not in dependencies or not dependencies[node]:
        memo[node] = 0
        return 0
    max_level = 0
    for child in dependencies[node]:
        max_level = max(max_level, compute_level(child, dependencies, memo))
    memo[node] = max_level + 1
    return max_level + 1

def dfs(node, dependencies, visited, order):
    if node in visited:
        return
    visited.add(node)
    if node in dependencies:
        for child in sorted(dependencies[node]):
            dfs(child, dependencies, visited, order)
    order.append(node)
for t in range(int(input())):
    D, E = map(int, input().strip().split())

    dependencies = {}

    for i in range(D):
        a, b = input().strip().split()
        if a in dependencies:
            dependencies[a].append(b)
        else:
            dependencies[a] = [b]
    
    for i in range(E):
        order = []
        visited = set()

        node = input().strip()

        dfs(node, dependencies, visited, order)
        
        memo = {}
        level_map = {node: compute_level(node, dependencies, memo) for node in visited}

        sorted_nodes = sorted(visited, key=lambda x: (level_map[x], x))
        for node in sorted_nodes:
            print("restart " + node)
        print("exit")

        

        
                
        