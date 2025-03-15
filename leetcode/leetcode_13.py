s = 'IX'

rum_numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

given_rum_numbers = list(s)

number = 0
i = 0
while i < len(given_rum_numbers):
    current_value = rum_numbers[given_rum_numbers[i]]

    if i + 1 < len(given_rum_numbers):
        next_value = rum_numbers[given_rum_numbers[i + 1]]
        if current_value < next_value:
            number += next_value - current_value
            i += 2  # Skip the next character
        else:
            number += current_value
            i += 1
    else:
        number += current_value
        i += 1

print(number)