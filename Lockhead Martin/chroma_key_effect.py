import math
for t in range(int(input())):
    Cr, Cg, Cb, T, Fr, Fg, Fb, Br, Bg, Bb = map(int, input().split())
    if math.sqrt((Cr-Fr)**2 + (Cg-Fg)**2 + (Cb-Fb)**2) <= T:
        print(f"{Br} {Bg} {Bb}")
    else:
        print(f"{Fr} {Fg} {Fb}")
    
