def pow_stars(num):
    if num > 0:
        return 2 * pow_stars(num-1)
    else:
        return "*"
    
print(pow_stars(3))