for t in range(int(input())):
    to_reverse = input().split()
    
    for index, word in enumerate(to_reverse):
        new = list(word)
        left = 0
        right = len(new) - 1
        while left < right:
            if not new[right].isalpha():
                right -= 1
            else:
                if new[left].upper() == new[left]:
                    if new[right].upper() == new[right]:
                        new[left], new[right] = new[right], new[left]
                    else:
                        new[left], new[right] = new[right].upper(), new[left].lower()
                elif new[right].upper() == new[right]:
                    new[left], new[right] = new[right].lower(), new[left].upper()
                    
                else:
                    new[left], new[right] = new[right], new[left]
                left += 1
                right -= 1
        to_reverse[index] = "".join(new)
        
    x = (" ".join(to_reverse))
    print(x.strip())
        
        