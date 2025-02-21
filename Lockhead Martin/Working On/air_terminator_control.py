from datetime import datetime

def time_to_minutes(time_str):
    """Convert HH:MM time format to total minutes."""
    hh, mm = map(int, time_str.split(":"))
    return hh * 60 + mm

for _ in range(int(input())):
    good, times = input().split()
    good = good == "TRUE"
    times = int(times)

    if good:
        print("NONE")
        for _ in range(times): 
            input()
        continue

    threat_levels = {1: "NONE", 2: "LOW", 3: "MEDIUM", 4: "HIGH"}
    timestamps = [time_to_minutes(input()) for _ in range(times)]

    threat_level = 1  

    if times >= 36:
        threat_level = max(threat_level, 4) 
    elif times >= 24:
        threat_level = max(threat_level, 3) 
    elif times >= 12:
        threat_level = max(threat_level, 2) 

    max_continuous = 1
    current_continuous = 1
    entry_count = 1  

    for i in range(1, times):
        if timestamps[i] - timestamps[i - 1] == 15:
            current_continuous += 1
        else:
            max_continuous = max(max_continuous, current_continuous)
            current_continuous = 1
            entry_count += 1

    max_continuous = max(max_continuous, current_continuous)

    if max_continuous >= 12:
        threat_level = max(threat_level, 4)  
    elif max_continuous >= 8:
        threat_level = max(threat_level, 3)  
    elif max_continuous >= 4:
        threat_level = max(threat_level, 2)  

    if entry_count >= 8:
        threat_level = max(threat_level, 4) 
    elif entry_count >= 4:
        threat_level = max(threat_level, 3) 

    print(threat_levels[threat_level])
