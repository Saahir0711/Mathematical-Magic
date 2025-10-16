decimal_number = int(input("Enter a decimal number:"))

binary = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary = str(remainder) + binary
    decimal_number = decimal_number // 2

print("Binary number is:", binary)

binary_number = input("Enter a binary number: ")

decimals = 0
power = 0

for digit in binary_number[::-1]:
    decimals += int(digit) * (2 ** power)
    power += 1

print("Decimal value is:", decimals)