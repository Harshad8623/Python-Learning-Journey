# Write a function tax_calculator(income) that takes annual income and returns the tax amount based on these slabs :
# up to 2,50,000 --> No Tax
# 2,50,000 to 5,00,000 --> 5%
# 5,00,000 to 10,00,000 --> 20%
# Above 10,00,000 --> 30%

def tax_calculator(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return (250000 * 0.05) + ((income - 500000) * 0.20)
    else:
        return (250000 * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)


print(tax_calculator(200000))
print(tax_calculator(400000))
print(tax_calculator(700000))
print(tax_calculator(1500000))