from datetime import datetime
def pluralize(value, unit, pad=False):
    formatted_value = f"{value:02d}" if pad else str(value)
    return f"{formatted_value} {unit}" if value == 1 else f"{formatted_value} {unit}s"

for s in range(int(input())):
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

    formatted_difference = " ".join([pluralize(days, "Day", pad=True), pluralize(hours, "Hour", pad=True), pluralize(minutes, "Minute",pad=True), pluralize(seconds, "Second",pad=True)])
    print(formatted_difference.strip())