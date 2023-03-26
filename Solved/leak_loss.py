import math
for t in range(int(input())):
  volume_of_pool, rate_of_fill, rate_of_leak = map(float, input().split())
  ans = (volume_of_pool/(rate_of_fill-rate_of_leak)*rate_of_leak)
  if ans - math.floor(ans)>=.5:
    print(math.ceil(ans))
  else:
    print(math.floor(ans))