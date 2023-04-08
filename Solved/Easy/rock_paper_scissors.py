for t in range(int(input())):
    answers = input().split()
    if "R" in answers and "P" in answers and "S" in answers:
        print("NO WINNER")
    elif "R" in answers and "S" in answers and answers.count("R") <= 1:
        print("ROCK")
    elif "P" in answers and "R" in answers and answers.count("P") <= 1:
        print("PAPER")
    elif "S" in answers and "P" in answers and answers.count("S") <= 1:
        print("SCISSORS")
    else:
        print("NO WINNER")