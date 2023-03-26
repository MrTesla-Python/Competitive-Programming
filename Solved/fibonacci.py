def fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans
d = {0:0, 1:1, 2:1}
for t in range(int(input())):
    n = int(input())
    print(str(n) + " = " + str(fib(n-1, d)))