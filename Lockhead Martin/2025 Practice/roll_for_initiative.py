for t in range(int(input())):
    num_c, num_s = map(int, input().split())

    stat_p = {}

    for _ in range(num_c):
        data = input().split()
        class_n = data[0]
        stat_p[class_n] = data[1:]
    
    for _ in range(num_s):
        class_s = {}
        data = input().split()
        class_n = data[0]
        stat_v = list(map(int, data[1:]))
        class_s[class_n] = sorted(stat_v, reverse=True)
    
        d = {"STR" : 0, "DEX" : 0, "CON" : 0, "INT" : 0, "WIS" : 0, "CHA" : 0}
        for key in class_s:
            print(key)
            for i, stat in enumerate(stat_p[key]):
                d[stat] = class_s[key][i]
            for i in d:
                print(i + ": " + str(d[i]))
