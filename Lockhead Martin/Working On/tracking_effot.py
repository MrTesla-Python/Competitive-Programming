def round_down_to_tenth(minutes):
    return math.floor(minutes * 10 / 60) / 10
import math
for t in range(int(input())):
    x = int(input())
    
    logs = []
    while True:
        entry = input().strip()
        if "End Day" in entry:
            task, time = entry.split("|")
            time = int(time.strip())
            logs.append((task.strip(), time))
            break
        else:
            task, time = entry.split("|")
            logs.append((task.strip(), int(time.strip())))

    total_time = {}
    for i in range(len(logs) - 1):
        activity, time = logs[i]
        next_activity, next_time = logs[i + 1]

        start_hour, start_min = divmod(time, 100)
        end_hour, end_min = divmod(next_time, 100)

        start_mins = start_hour * 60 + start_min
        end_mins = end_hour * 60 + end_min

        if end_mins < start_mins:
            end_mins += 24*60
        time_spent = end_mins - start_mins


        activity = activity.strip()

        if activity not in total_time:
            total_time[activity] = 0
        total_time[activity] += time_spent

    for activity in sorted(total_time):
        
        print(f"{activity}-{round_down_to_tenth(total_time[activity]):.1f}")