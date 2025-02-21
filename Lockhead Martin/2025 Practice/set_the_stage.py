for t in range(int(input())):

    y, x = map(int, input().split(","))

    d, m, q = map(int, input().split(","))

    req_d = req_m = req_q = 0

    nums = []

    for i in range(y):
        new = input().split(",")
        nums += new

    for num in nums:
        num = float(num)
        if num > 0:
            req_d += 1
            whole = int(num)
            req_m += whole
            frac = round(num - whole, 2)
            if frac > 0:
                req_q += int(round(frac/.25))
    

    missing_m = max(0, req_m - m)

    extra_quarter = max(0, q - req_q)

    substitute = min(missing_m, extra_quarter // 4)

    req_m -= substitute
    req_q += substitute*4

    used_d = min(d, req_d)
    used_m = min(m, req_m)
    used_q = min(q, req_q)

    spare_d = d - req_d
    spare_m = m - req_m
    spare_q = q - req_q

    print(f"{used_d} ({spare_d}),{used_m} ({spare_m}),{used_q} ({spare_q})")
