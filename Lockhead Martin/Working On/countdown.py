from datetime import datetime
def pluralize(value, unit):
    return f"{value} {unit}" if value == 1 else f"{value} {unit}s"
for s in range(int(input())):
    timestamps = []
    x, y = input().split("|")
    x= x.strip()
    y = y.strip()
    # Convert to datetime objects
    x = (datetime.strptime(x, "%m.%d.%Y %H:%M:%S"))
    y = (datetime.strptime(y, "%m.%d.%Y %H:%M:%S"))

   
    differences = y-x
    days = differences.days
    seconds = differences.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    formatted_difference = ", ".join([pluralize(days, "Day"), pluralize(hours, "Hour", pad), pluralize(minutes, "Minute"), pluralize(seconds, "Second")])
    print(formatted_difference)