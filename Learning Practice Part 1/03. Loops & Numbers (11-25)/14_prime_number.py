n = int(input("Enter a number : "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")



n = int(input("Enter a number : "))
count = 0
for i in range(1, (n // 2) + 1):
    if n % i == 0:
        count += 1
if count == 1:
    print("Prime")
else:
    print("Not Prime")




n = int(input("Enter a number : "))
count = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        count += 1
if n > 1 and count == 1:
    print("Prime")
else:
    print("Not Prime")