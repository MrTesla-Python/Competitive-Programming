tree = {}
nodes = set()
root = None
for t in range(int(input())):
    child, parent = input().strip().split(",")
    nodes.add(child)
    if parent != "None":
        nodes.add(parent)
        tree.setdefault(parent, []).append(child)
    else:
        root = child
    
    for node in nodes:
        tree.setdefault(node, [])
    
    for parent in tree:
        tree[parent] = sorted(tree[parent])


def dfs(node, depth):
    print("-" * depth + node)
    for child in sorted(tree[node]):
        dfs(child, depth + 1)
    

dfs(root, 0)