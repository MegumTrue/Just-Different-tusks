dictionary = {'a': 1, "b": 2, "c": 3}
numbers = [1, 2, 3, 4, 5, 6]
lst = ['a', 'b', 'c', 'd', 'f', 'g']

dict1 = {key:value for (key, value) in dictionary.items()}
num_dict = {num: num**2 if num % 2== 0 else "null" for num in numbers}
dual_dict = {s: num for s, num in zip(lst, numbers)}
simpl_dict = {k: n for n in range(1, 10) for k in range(0, 9)}
'''
print(dict1)
print(num_dict)
print(dual_dict)
print(simpl_dict)'''
