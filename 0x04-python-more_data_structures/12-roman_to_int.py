#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or len(roman_string) is 0:
        return 0

    roman_numbers = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000
    }
    output, loops, prev = 0

    for key in roman_string:
        if loops > 0 and prev < roman_numbers[key]:
            output -= prev
            output = output + (roman_numbers[key] - prev)
        else:
            output = output + roman_numbers[key]

        loops += 1
        prev = roman_numbers[key]
    return output
