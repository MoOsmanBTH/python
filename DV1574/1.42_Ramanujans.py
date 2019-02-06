import math

def faculty(number):
    if number > 0:
        return faculty(number - 1) * number
    else: 
        return 1

def estimate_pi():
    
    ram_iteration = 0
    k = 0
    sum = 0
    while sum < 10**(-15):
        sum = (faculty(4 * k) * (1103 + 26390 * k)) /\
        ((faculty(k)**4) * (396**(4*k)))
        ram_iteration += sum
    return 9801 / (2*math.sqrt(2)*ram_iteration)


print(estimate_pi())