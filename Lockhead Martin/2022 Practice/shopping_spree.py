import math
def round_half_up(n, decimals=0):
    factor = 10 ** decimals
    return math.floor(n * factor + 0.5) / factor
for t in range(int(input())):
    item, c = map(int, input().split())
    foods = {}
    for i in range(item):
        q, food, ch = map(str, input().split())
        foods[food] = [int(q), float(ch)]

    carts = {}
    for j in range(int(c)):
        line = input().split()
        customer = int(line[0])
        command = line[1]

        if command == "ADD":
            item = line[2]
            qty = int(line[3])
            if customer not in carts: carts[customer] = {}
            current = carts[customer].get(item, 0)
            if current + qty <= foods[item][0]:
                carts[customer][item] = current + qty
                print(f"Added {qty} {item} to customer {customer}'s cart")
            else:
                print(f"Not enough {item} for customer {customer}")

        elif command == "REMOVE":
            item = line[2]
            qty = int(line[3])
            if customer not in carts or carts[customer].get(item, 0) < qty:
                print(f"Customer {customer} does not have that many {item}s")
            else:
                carts[customer][item] -= qty
                print(f"Removed {qty} {item} from customer {customer}'s cart")
            
        elif command == "CHECKOUT":
            if customer not in carts:
                carts[customer] = {}
            short = []
            total = 0.0
            for item in carts[customer]:
                want = carts[customer][item]
                if (foods[item][0] < want):
                    short.append(item)
                else:
                    total += want * foods[item][1]
                    foods[item][0] -= carts[customer][item]
            for item in sorted(short):
                print(f"Out of stock of {item}")

            print(f"Customer {customer}'s total: ${round_half_up(total, 2):.2f}")
        
    for food in sorted(foods):
        if foods[food][0] > 0:
            print(f"{food} - {foods[food][0]}")