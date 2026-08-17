# Take a studsent's marks as input and print the corresponding grade based on the following criteria:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 50-59: E
# Below 50: F
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You got an A grade.")
elif marks >= 80:
    print("You got a B grade.")
elif marks >= 70:
    print("You got a C grade.")
elif marks >= 60:
    print("You got a D grade.")
elif marks >= 50:
    print("You got an E grade.")
else:
    print("You got a F grade.")