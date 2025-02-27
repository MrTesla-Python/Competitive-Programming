for t in range(int(input())):
    W, T, P = map(int, input().split())
    work_nums = []
    part_nums = []
    tasks = {}
    for i in range(W):
        new_work = input().split(",")
        work_nums.append(int(new_work[0]))
    for i in range(T):
        new_task = input().split(",")
        tasks[int(new_task[0])] = (int(new_task[1]), int(new_task[2]))
    for i in range(P):
        new_part = input().split(",")
        part_nums.append(int(new_part[0]))
    
    for task in sorted(tasks):
        if tasks[task][0] not in work_nums and tasks[task][1] not in part_nums:
            print(f"{task} MISSING WORK_ORDER {tasks[task][0]} MISSING PART {tasks[task][1]}")
        elif tasks[task][0] not in work_nums:
            print(f"{task} MISSING WORK_ORDER {tasks[task][0]}")
        elif tasks[task][1] not in part_nums:
            print(f"{task} MISSING PART {tasks[task][1]}")
    