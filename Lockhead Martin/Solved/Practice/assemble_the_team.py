for t in range(int(input())):
    text = input().split()
    agents = []
    for i in range(len(text)):
        letter, num = text[i].split("=")
        agents.append((letter, int(num)))
    agents.sort(key=lambda x: x[1])
    left = 0
    count = 0
    full_ans = []
    temp_ans = []
    for right in range(len(agents)):
        count = agents[right][1] - agents[left][1]
        while count > 10:
            temp_ans.remove(agents[left][0])
            left += 1
            count = agents[right][1] - agents[left][1]
        
        temp_ans.append(agents[right][0])
        if len(temp_ans) > len(full_ans):
            full_ans = temp_ans[:]
        elif len(temp_ans) == len(full_ans):
            for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if i in temp_ans and i not in full_ans:
                    full_ans = temp_ans[:]
                    break
                elif i in full_ans and i not in temp_ans:
                    break
    print(" ".join(sorted(full_ans)))
            
        

