def check_winner(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != '-':
            return game[i][0]
        if game[0][i] == game[1][i] == game[2][i] != '-':
            return game[0][i]
    
    if game[0][0] == game[1][1] == game[2][2] != '-':
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] != '-':
        return game[0][2]
    

for t in range(int(input())):
    test = list(input())
    game = [[j for j in test[i:i+3]] for i in range(0, len(test), 3)]
    if check_winner(game) == None:
        print(f"{''.join(test)} = TIE")
    else:
        print(f"{''.join(test)} = {check_winner(game)} WINS")
    