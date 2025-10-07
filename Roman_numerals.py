def roman_to_int(roman_number):
    roman_values = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    total = 0 

    for i in range(len(roman_number)):

        if i + 1 < len(roman_number) and roman_values[roman_number[i]] < roman_values[roman_number[i +1]]:
            total = total - roman_values[roman_number[i]]
        else:
            total = total + roman_values[roman_number[i]]

    return total

roman_input = input("Enter a Roman numeral: ")
print("Integer form of", roman_input, "is", roman_to_int(roman_input))