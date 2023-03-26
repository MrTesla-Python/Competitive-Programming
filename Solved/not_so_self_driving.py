for t in range(int(input())):
  v, d = map(float, input().split(":"))
  if v == 0:
    print("SAFE")
  elif d/v <= 1:
    print("SWERVE")
  elif 5 >= d/v > 1:
    print("BRAKE")
  else:
    print("SAFE")