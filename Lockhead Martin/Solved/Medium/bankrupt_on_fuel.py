from fractions import Fraction
for t in range(int(input())):
    fuel_available, rocket_counts = map(int, input().split())
    rockets = input().split()
    contents = len(rockets) * [0]
    contents = list(contents)
    highest_fuel = 0
    while fuel_available >= rocket_counts:
        for i in range(len(contents)):
            if contents[i] < int(rockets[i]):
                contents[i] +=1
                fuel_available -= 1
                if contents[i] == int(rockets[i]):
                    rocket_counts-=1
    for i in range(len(contents)):
        if contents[i] != int(rockets[i]):
            contents[i] += fuel_available/rocket_counts
    ans = ""
    for i in contents:
        ans += " " + str(Fraction(i).limit_denominator())
    print(ans.strip())