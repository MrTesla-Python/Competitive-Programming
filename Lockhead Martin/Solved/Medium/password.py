import re
for t in range(int(input())):
    password = input()
    uppercase = sum(1 for i in password if i.isupper())
    lowercase = sum(1 for i in password if i.islower()) 
    numbers = sum(1 for i in password if i.isnumeric())
    non_alpha = sum(1 for i in password if not i.isalnum())
    c = 0
    if uppercase > 0:
        c+=1
    if lowercase > 0:
        c+=1
    if numbers > 0:
        c+=1
    if non_alpha > 0:
        c+=1
    ans = ""
    two = not bool(re.search(r"(.)\1\1", password))
    if two == False or len(password) < 8 or c < 3:
        print("INVALID")
    else:
        print("VALID")