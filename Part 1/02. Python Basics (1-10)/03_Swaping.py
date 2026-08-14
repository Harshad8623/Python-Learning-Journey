# With using third variable
a = 10
b = 20
print("Before swapping: a =", a, "b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)



# Using tuple unpacking
p = 10
q = 20
print("Before swapping: p =", p, "q =", q)
p, q = q, p
print("After swapping: p =", p, "q =", q)


# Using XOR operator
m = 10
n = 20
print("Before swapping: m =", m, "n =", n)
m = m ^ n
n = m ^ n
m = m ^ n
print("After swapping: m =", m, "n =", n)


# Using arithmetic operations
i = 10
j = 20
print("Before swapping: i =", i, "j =", j)
i = i + j
j = i - j
i = i - j
print("After swapping: i =", i, "j =", j)