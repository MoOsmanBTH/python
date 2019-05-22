def use_function(function, number):
    return function(number) ** 2 

print(use_function(lambda x: x + 1, 4))