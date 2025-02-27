def pluralize(n, s):
    return s + "s" if n != 1 else s
for t in range(int(input())):
    s = input().split(",")
    name = s[0]
    times = s[1:]
    total = 0
    for time in times:
        hours, mins = time.split(":")
        total += int(hours) * 60 + int(mins)
    hours = total // 60
    mins = total % 60
    if (mins == 0):
        print(f"{name}={hours} {pluralize(hours, 'hour')}")
    else:
        print(f"{name}={hours} {pluralize(hours, "hour")} {mins} {pluralize(mins, 'minute')}")