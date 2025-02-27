def counting_out_rhyme(n, k, start):
    players = list(range(1, n + 1))
    i = start - 1
    while len(players) > 1:
        i = (i + k - 1) % len(players)
        players.pop(i)
    return players[0]

for t in range(int(input())):
    n, k = map(int, input().split())
    for i in range(1, n+1):
        winner = counting_out_rhyme(n, k, i)
        if winner == 1:
            print(i)
            break