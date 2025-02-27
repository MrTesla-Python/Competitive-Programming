for t in range(int(input())):
    d = {}
    happens = int(input())
    for i in range(happens):
        entry, name, time, event_id, team = (input().split(","))

        if event_id not in d:
            d[event_id] = {"Day" : 0, "Night" : 0}
        if team.strip() == "true":
            if time == "Day":
                d[event_id]["Day"] += 1
            else:
                d[event_id]["Night"] += 1
    for event_id in d:
        day = d[event_id]["Day"]
        night = d[event_id]["Night"]
        print(f"{event_id},{d[event_id]["Day"]},{d[event_id]["Night"]}")