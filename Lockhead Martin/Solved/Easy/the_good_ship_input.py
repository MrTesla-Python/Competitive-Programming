for t in range(int(input())):
  foo = input().rstrip()
  fooParts = foo.split(" ")
  databaseCount = int(fooParts[0])
  shipCount = int(fooParts[1])
  database = []
  for i in range(databaseCount):
    database.append(input())
  for i in range(shipCount):
    database.remove(input())
  database.sort(key=str.lower)
  for system in database:
    print(system)