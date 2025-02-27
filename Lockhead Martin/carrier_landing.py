for t in range(int(input())):
    for i in range(int(input())):
        airplane = input()
        x, y = map(float, input().split(","))
        x_start, y_start = map(float, input().split(","))
        x_end, y_end = map(float, input().split(","))
    
        slope_start = (y_start - y) / (x_start - x)
        slope_end = (y_end - y) / (x_end - x)
    
        if .8 <= abs(slope_start) <= 1.6 and .8 <= abs(slope_end) <= 1.6:
            print(f"{airplane.strip()}, Clear To Land!")
        else:
            print(f"{airplane.strip()}, Abort Landing!")