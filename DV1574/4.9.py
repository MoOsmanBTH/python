fib = [0, 1]
 
for a in range(2, int(input("How many iterations (x>1): "))):
    fib.append(fib[a-1]+ fib[a-2])
print(list(map(lambda x: x**2,fib)))

