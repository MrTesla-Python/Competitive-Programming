import sys
def eliminate(n, k, s):
    # n is the number of people, k is the elimination index
    people = list(range(n))
    i = s 
    while len(people) > 1:
        i = (i + k - 1) % len(people)
        people.pop(i)
    return people[0]
t = int(sys.stdin.readline())
for x in range(t):
    n, k = map(int, input().split())
    for i in range(n):
        winner = eliminate(n, k, i)
        if winner == 1:
            print(i)