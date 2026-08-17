# Create a dictionary mapping five countries to their capital cities. Iterate through this dictionary using the items() method and print each pair in the format: Country → Capital.

countries = {
    "India": "Delhi",
    "South Africa": "Pretoria",
    "Australia": "Canberra",
    "Pakistan": "Islamabad",
    "Nepal": "Kathmandu"
}

for country, capital in countries.items():
    print(country, "→", capital)