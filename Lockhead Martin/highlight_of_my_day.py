import math
def round_half_up(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor
for t in range(int(input())):
    sent = input().strip()
    highlight_color = [int(i) for i in sent[1:-1].split(",")]
    C, R= map(int, input().split())
    grid_pixels = []
    grid_rgb = []
    for i in range(R):
        grid_pixels.append(list(map(int, input().strip().split())))
        
    for i in range(R):
        grid_rgb.append([list(map(int, pixel.strip("()").split(","))) for pixel in input().split()])
    
    vertices = ((-1, 0),(1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))
    
    for i in range(R):
        for j in range(C):
            if grid_pixels[i][j] == 1:
                p = 0.5
            else:
                p = 0.0
                for di, dj in vertices:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < R and 0 <= nj < C and grid_pixels[ni][nj] == 1:
                        p = 1.0
                        break
            for k in range(3):
                grid_rgb[i][j][k] = int(round_half_up((1-p) * grid_rgb[i][j][k] + p * highlight_color[k]))
                    
    for i in range(R):
        ans = ""
        for j in range(C):
            ans += f"({grid_rgb[i][j][0]},{grid_rgb[i][j][1]},{grid_rgb[i][j][2]}) "
        print(ans.strip())
        ans = ""
    