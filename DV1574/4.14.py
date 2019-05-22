def coord3D_sum_not_n(x, y, z, n):
    return [[a, b, c] for a in range(x + 1) for b in range(y+1) for c in range(z+1) if a + b + c != n]

print(coord3D_sum_not_n(2, 2, 2, 2))

