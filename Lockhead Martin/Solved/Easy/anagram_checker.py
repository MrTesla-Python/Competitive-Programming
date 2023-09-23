for t in range(int(input())):
  s = input()
  a, b = map(str, s.split("|"))
  if a == b:
    print(s+ " = NOT AN ANAGRAM")
  elif sorted(a) == sorted(b):
    print(s+" = ANAGRAM")
  else:
    print(s+ " = NOT AN ANAGRAM")