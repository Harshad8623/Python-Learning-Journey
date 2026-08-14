sum = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        continue
    elif num == 0:
        break
    else:
        sum += num
print("The sum of positive numbers is:", sum)

# nested loop
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()