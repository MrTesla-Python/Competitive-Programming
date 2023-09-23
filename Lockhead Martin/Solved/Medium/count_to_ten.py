for t in range(int(input())):
    count = int(input())
    curr = 0
    while True:
        curr_bin = bin(curr)
        curr_bin = int(curr_bin[2:])
        if len(str(curr_bin)) <= count:
            print("{:0{}d}".format(curr_bin, count))
        else:
            break
        curr+=1