from itertools import permutations

def find_combinations(candidates, target):
    candidates.sort()

    res = []

    def backtrack(cur, pos, target):
        if target == 0:
            res.append(cur.copy())
            return
        if target <= 0:
            return

        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur, i + 1, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtrack([], 0, target)
    return res

for t in range(int(input())):
    res = []
    target = input()
    target = target[9:]
    target = int(target)
    nums = input().split(",")
    nums = [int(i) for i in nums]
    combs = find_combinations(nums, target)
    for comb in combs:
        for perm in permutations(comb):
            res.append(perm)
    res = list(set(res))
    res = sorted(res)
    for comb in res:
        print("+".join(map(str, comb)))