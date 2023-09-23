def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
for t in range(int(input())):
    n = int(input())
    print(factorial(n))