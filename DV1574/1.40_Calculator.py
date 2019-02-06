def add(num1 = 0, num2 = 0):
    return "%d + %d = %d" % (num1, num2, (num1 + num2))

def subtract(num1 = 0, num2 = 0):
    return "%d - %d = %d" % (num1, num2, (num1 - num2))

def divide(num1 = 0, num2 = 1):
    ret_value = ""
    if num2 != 0: 
        ret_value = "%d / %d = %d" % (num1, num2, (num1 / num2))
    else:
        ret_value = "Error, can't divide by 0"

    return ret_value
    
def multiply(num1 = 0, num2  = 0):
    return "%d * %d = %d" % (num1, num2, (num1 * num2))

exit_state = False

menu_text = "\n1. Enter two integers\n\
2. Add\n3. Subtract \n4. Multiply\n5. Divide\n\
0. Exit\nYour choice: "
wrong_input_message = "Input must be either 0, 1, 2, 3, 4 or 5"
number_1, number_2 = 0, 0

while exit_state == False:
    user_input = int(input(menu_text))
    
    if(user_input == 0):
        exit_state = True

    elif user_input == 1:
        number_1 = int(input("Integer 1: "))
        number_2 = int(input("Integer 2: "))

    elif user_input == 2:
        print(add(number_1, number_2))

    elif user_input == 3:
        print(subtract(number_1, number_2))

    elif user_input == 4:
        print(multiply(number_1, number_2))

    elif user_input == 5:
        print(divide(number_1, number_2))

    else:
        print(wrong_input_message)