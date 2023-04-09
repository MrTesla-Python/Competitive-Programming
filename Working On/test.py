lst = [['A', '10'], ['B', '22'], ['C', '15'], ['D', '18'], ['E', '4']]
my_dict = {key: int(value) for key, value in lst}
print(my_dict)