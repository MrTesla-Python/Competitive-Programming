import math
import decimal
def round_to_nearest_decimal(number):
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    return float(decimal.Decimal(str(number)).quantize(decimal.Decimal('.001')))

for i in range(int(input())):
    x, y, h, step = map(float, input().split())
    for i in range(int(step)):
        y = y + h * (math.sin(x)/x)
        x = h + x
    print(round_to_nearest_decimal(y))