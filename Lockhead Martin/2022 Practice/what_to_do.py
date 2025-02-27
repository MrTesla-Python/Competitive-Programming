for t in range(int(input())):
    c, t = map(int, input().split(","))

    tasks = []
    for i in range(t):
        description, priority, start_cycle, duration = map(str, input().split(","))
        priority = int(priority)
        start_cycle = int(start_cycle)
        duration = int(duration)

        tasks.append(({
            "description": description,
            "priority": priority,
            "start_cycle": start_cycle,
            "remaining": duration,
            "order": i
                       }))
        
    for i in range(1, c+1):
        candidates = [task for task in tasks if task["remaining"] > 0 and task['start_cycle'] <= i]

        if not candidates:
            print(f"{i},Wait")
        else:
            best_task = max(candidates, key=lambda t: (t["priority"], -t["order"]))
            best_task['remaining'] -= 1
            print(f"{i},{best_task['description']}")
    
