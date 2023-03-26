# working on
for t in range(int(input())):
    old, new = map(int, input().split())
    old_l = []
    new_l = []
    for i in range(old):
        old_l.append(input().split(","))
    for i in range(new):
        new_l.append(input().split(","))
    for i in new_l:
        if i[0] in old_l:
            print("t")
        else:
            print("f")