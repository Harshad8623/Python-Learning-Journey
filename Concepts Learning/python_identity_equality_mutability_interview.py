#Python notes on : identity, equality, mutability, and objects.

# 1. is versus ==
a = -12
b = -12
print(a is b)  # Commonly True in CPython; do not rely on it
print(a == b)  # True: equal values

# CPython commonly reuses small integers from -5 through 256.
# This is an implementation detail, not a Python language guarantee.
x = 1000
y = 1000
print(x is y)  # Do not rely on the result
print(x == y)  # True

# 2. Large float constants
a = 10000000000000000000000000082752482.285
b = 10000000000000000000000000082752482.285
print(a is b)  # May be True in the same compiled code block
print(a == b)  # True
# The compiler may reuse identical constants in a code object.
# Python float uses limited binary precision; do not rely on float identity.


a = int("500")
b = int("500")

print(a is b) # True
print(a == b) # True

"""
Important concept
CPython commonly caches integers from -5 to 256. However, 500 is outside that range.

So why can is still return True?
Because the compiler may reuse identical constants. Integer caching is not the only optimization.
"""

a = int("500")
b = int("500")

print(a is b) # False
print(a == b) # True

# 3. Lists: equal contents, different objects
a = [10, 20, 30]
b = [10, 20, 30]
print(a is b)  # False: separate objects
print(a == b)  # True: equal contents
c = a
print(a is c)  # True: both names refer to the same list
c.append(40)
print(a)       # [10, 20, 30, 40]

# 4. id() returns an identity value unique during the object lifetime.
# In CPython it is commonly the memory address, but Python does not require that.
first = [1, 2]
second = [1, 2]
third = first
print(id(first), id(second), id(third))
print(first is second)  # False
print(first is third)   # True

# 5. Strings and interning
s1 = "python"
s2 = "python"
print(s1 == s2)  # True
print(s1 is s2)  # May be True due to reuse/interning
s3 = "".join(["py", "thon"])
print(s3 == s1)  # True
print(s3 is s1)  # Do not rely on this result
# Strings are immutable. Use == for comparing their values.

# 6. Tuples
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 == t2)  # True
print(t1 is t2)  # Identity is not guaranteed
# A tuple is immutable as a container, but can contain mutable objects.
t3 = ([1, 2], "hello")
t3[0].append(3)
print(t3)  # ([1, 2, 3], "hello")

# 7. Dictionaries and sets
d1 = {"a": 1}
d2 = {"a": 1}
print(d1 == d2)  # True
print(d1 is d2)  # False
set1 = {1, 2, 3}
set2 = {3, 2, 1}
print(set1 == set2)  # True; sets are unordered
print(set1 is set2)  # False

# 8. Mutable versus immutable types
# Common immutable: int, float, bool, complex, str, bytes, tuple, frozenset.
# Common mutable: list, dict, set, bytearray.
number = 10
alias = number
alias = 20
print(number)  # 10; rebinding alias does not change number
items = [10, 20]
alias_items = items
alias_items.append(30)
print(items)  # [10, 20, 30]; both names refer to the same list

# 9. Shallow copy versus deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
print(original is shallow)        # False
print(original[0] is shallow[0])  # True: nested list is shared
print(original[0] is deep[0])     # False: nested list is copied
shallow[0].append(99)
print(original)  # Original changes because inner list is shared
deep[1].append(88)
print(original)  # Original second inner list is unaffected

# 10. None and booleans
result = None
print(result is None)  # True; recommended
print(result == None)  # True, but is None is preferred
x = True
y = True
print(x is y)  # True
print(x == y)  # True
# None, True, and False are singleton objects.

# 11. Floating-point precision
print(0.1 + 0.2)         # Commonly 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
# Use Decimal("0.1"), not Decimal(0.1), for exact decimal input.

# 12. NaN (Not a Number)
nan = float("nan")
print(nan == nan)  # False: NaN is not equal to itself
print(nan is nan)  # True: same object reference
print(math.isnan(nan))  # True: recommended NaN check

# 13. Custom equality using __eq__
class Person:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name

p1 = Person("Asha")
p2 = Person("Asha")
print(p1 == p2)  # True: custom equality compares names
print(p1 is p2)  # False: different objects
# `is` cannot be customized; `==` can call __eq__.

# INTERVIEW SUMMARY
# is: checks whether references point to the same object.
# ==: checks equality according to the type / __eq__ implementation.
# Mutability: whether an object can change after creation.
# Interning: implementation optimization that reuses some immutable objects.
# Shallow copy: new outer object, nested objects shared.
# Deep copy: recursively copies nested objects.
# Use == for values; use is for identity, especially `value is None`.
# Never depend on is results for ordinary numbers, strings, or tuples.

# COMMON INTERVIEW QUESTIONS
# 1. Difference between is and ==? Identity versus value equality.
# 2. Why can equal lists return False with is? They may be distinct objects.
# 3. What does id() do? Returns an identity value unique during object lifetime.
# 4. What is interning? Reusing some immutable objects as an optimization.
# 5. Are small integers cached? CPython commonly reuses -5 to 256; implementation detail.
# 6. Why use is None? None is a singleton; identity is the recommended test.
# 7. What is mutability? Whether an object state can change.
# 8. Shallow vs deep copy? Shallow shares nested objects; deep recursively copies.
# 9. Can is be customized? No; == can be customized with __eq__.
# 10. Why is 0.1 + 0.2 not exactly 0.3? Binary floating-point representation limits.
