for t in range(int(input())):
    cities = int(input())
    city_map = {}
    for i in range(cities):
        city, destination = input().split()
        if city not in city_map:
            city_map[city] = destination
    
    start = ""
    end = ""
    for city in city_map:
        if city not in city_map.values():
            start = city
            break
    for city in city_map.values():
        if city not in city_map:
            end = city
            break
    
    path = []
    while len(path) < cities:
        path.append(start)
        start = city_map[start]
    path.append(end)
    
    for i in reversed(path):
        print(i)