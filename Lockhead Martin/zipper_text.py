for _ in range(int(input())):
    U = int(input().strip())
    upper_lengths = list(map(int, input().split()))
   
    L = int(int(input().strip()))
    lower_lengths = list(map(int, input().split()))
  

    encoded_message = []
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            encoded_message.append(line)
        except:
            break
    encoded_message = "".join(encoded_message)

    lower_message = []
    upper_message = []

    upper = ""
    lower = ""
    
    count_upper = 0
    count_lower = 0
    for char in encoded_message:
        if char.isupper() or char == "-":
            upper += char
        elif char.islower() or char == "=":
            lower+=char
        if count_upper > len(upper_lengths)-1:
            continue
        else:

            if len(" ".join(upper.split("-"))) == upper_lengths[count_upper]:
                upper_message.append(" ".join(upper.strip().split("-")))
                upper = ""
                count_upper+=1
        if count_lower > len(lower_lengths)-1:
            continue
        else:
            if len(" ".join(lower.split("="))) == lower_lengths[count_lower]:
                #print(lower_message)
                lower_message.append(" ".join(lower.strip().split("=")))
                lower = ""
                count_lower+=1
      
    for i in upper_message:
        print(i.strip())
    print()
    for i in lower_message:
        print(i.strip())
