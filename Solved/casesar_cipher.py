import string
for t in range(int(input())):
  shift = int(input())
  sent = input()
  lower_keys = list(string.ascii_lowercase)
  lower_values = list(string.ascii_lowercase)
  lower_values = lower_values[shift:]+lower_values[:shift]
  full_dict = dict(zip(lower_values, lower_keys))
  ans = ""
  for i in sent:
    if i in full_dict.keys():
      ans += full_dict[i]
    else:
      ans += i
  print(ans)