# Write a Python function named merge_dicts(d1, d2) that accepts two dictionaries (d1 and d2) as arguments and returns a new dictionary formed by merging them using the update() method. Ensure d1 remains unchanged.

def merge_dicts(d1, d2):
    d3 = {}
    d3.update(d1)
    d3.update(d2)
    return d3

print(merge_dicts(
    {"Name": "Harshad", "Marks": 98},
    {"Age": 21}
))