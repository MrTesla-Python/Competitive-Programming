import math
def round(num, decimals=0):
    factor = 10 ** decimals
    return math.floor(num * factor + 0.5) / factor
for t in range(int(input())):
    items, cases = map(int, input().split())
    compare = {}
    for i in range(items):
        item, radi = input().split()
        radi = float(radi)
        compare[item] = radi

    for i in range(cases):
        item, thickness, absorption = input().split()
        thickness = float(thickness)
        absorption = float(absorption)

        total = compare[item] * thickness
        if total >= absorption:
            print("Infinity")
        else:
            ans = 50/(absorption-total)
            print(f"{round(ans, 2):.2f}")
