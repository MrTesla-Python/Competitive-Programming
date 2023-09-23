for t in range(int(input())):
    x,y,z = map(float, input().split())
    if x - 180 < 0:
        x+=180
    else:
        x-=180
    if y - 180 < 0:
        y+=180
    else:
        y-=180
    if z - 180 < 0:
        z+=180
    else:
        z-=180
    print("{:0>6.2f}".format(x),"{:0>6.2f}".format(y),"{:0>6.2f}".format(z))