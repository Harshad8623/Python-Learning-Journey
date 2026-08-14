# Write a function power(base, exp) that returns base raised to exp using a loop - no ** operator or pow() allowed
def powerA(base, exp):
    prod = 1
    for i in range(exp):
        prod *= base
    return prod
print(powerA(2, 3))



def powerB(base, exp):
    prod = 1
    if exp > 0:
        for i in range(exp):
            prod *= base
    elif exp == 0:
        return prod
    else:
        for i in range(abs(exp)):
            prod *= base
        return 1 / prod
    return prod
print(powerB(2, 3))
print(powerB(2, 0))
print(powerB(2, -3))