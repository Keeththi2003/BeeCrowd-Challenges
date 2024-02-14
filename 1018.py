# Read the integer value from the user input
value = int(input())

# List of available banknotes
banknotes = [100, 50, 20, 10, 5, 2, 1]

print(value)

# Calculate and print the minimum quantity of each necessary banknote
for banknote in banknotes:
    quantity = value // banknote
    print(f"{quantity} nota(s) de R$ {banknote},00")
    value %= banknote