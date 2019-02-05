def fibonacci(iterations):
    ret_value = []
    ret_value.append(0)
    ret_value.append(1)

    for i in range(1, iterations, 1):
        temp = ret_value[i] + ret_value[i - 1]
        ret_value.append(temp)
    return ret_value

def fibonacci_to_string(iterations):
    numbers = fibonacci(iterations)
    ret_value = "%d" % numbers[0]
    for i in range(1, iterations, 1):
        ret_value += ", %d" % numbers[i]

    return ret_value 

user_input = int(input("Input number: "))
print(fibonacci_to_string(user_input))