for t in range(int(input())):
    altitudes = int(input())
    prev_elevation = 0
    prev_altitude = 0
    for i in range(altitudes):
        altitude, elevation = map(int, input().strip().split(","))
        next_altitude = altitude - prev_altitude
        if altitude+next_altitude <= elevation:
            print("PULL UP!")
        elif altitude - prev_elevation <= 500:
            print("Low Altitude!")
        else:
            print("ok")
        prev_elevation = elevation
        prev_altitude = altitude
        