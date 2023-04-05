def pascal_row(n):
    row = [1]
    for i in range(1, n+1):
        next_val = row[-1] * (n-i+1) // i
        row.append(next_val)
    return row


for t in range(int(input())):
    print(max(pascal_row(int(input()))))