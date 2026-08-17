# Take a list of names as input (comma separated). Split them, sort them alphabetically, and join them back with " | " as separator.

names = input("Enter names separated by comma: ")

names = names.split(",")
names.sort()
result = " | ".join(names)
print(result)