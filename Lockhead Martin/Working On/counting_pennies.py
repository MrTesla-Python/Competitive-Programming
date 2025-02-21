import decimal
def round_to_nearest_decimal(number):
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP
    return float(decimal.Decimal(str(number)).quantize(decimal.Decimal('.01')))
for s in range(int(input())):
    orders = int(input())
    ans = 0
    for order in range(orders):
        new = float(input())
        if (int(new) == new):
            print(int(new))
        else:
            ans += int(new) + 1 - new
            print(int(new)+1)
    print("%.2f" % round_to_nearest_decimal(ans))