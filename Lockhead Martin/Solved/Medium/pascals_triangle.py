def pascal_row(n):
    if n == 0:
        return [1]
    else:
        prev_row = pascal_row(n-1)
        return [1] + [prev_row[i] + prev_row[i+1] for i in range(n-1)] + [1]
for t in range(int(input())):
    print(max(pascal_row(int(input()))))