# Construct a dictionary containing four product names and their prices. Prompt the user to enter a product name. Use the in keyword to check if it exists; if so, display its price. Otherwise, inform the user "Product not found."

products = {
    "Book": 150,
    "Pen": 10,
    "Notebook": 180,
    "Bag": 780
}

name = input("Enter the Product Name : ")

if name in products:
    print(products[name])
else:
    print("Product not found.")