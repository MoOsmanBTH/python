a = input("float a: ")
b = input("float b: ")

try:  
    print(float(a)/float(b))
except ZeroDivisionError as error:
    print("Error message: ", error)
except ValueError as error: 
    print("Error message: ", error)
