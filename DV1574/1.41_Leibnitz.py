number = 0.0
for i in range(0, 2000000, 1):
    number += ((-1)**i) / ((2 * i) + 1)
number *= 4
print(number)