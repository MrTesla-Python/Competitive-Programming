for t in range(int(input())):
    doors_start,rounds,doors_round=[int(i) for i in input().split()]
    doors=doors_start
    prob_prize=100.0/doors_start
    for rnd in range(rounds):
        doors -= 1
        wrong_guess = prob_prize*doors
        doors -= doors_round
        prob_prize = wrong_guess/doors
    prob_prize = prob_prize/100
    print("{:.2%}".format(prob_prize))