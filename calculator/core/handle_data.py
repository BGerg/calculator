import calculator.core.numbers as numbers
import sys

def convert_expression_to_arabic(roman_expression: str):
    roman_number = ""
    arabic_expression = ""
    for elem in roman_expression:
        if elem == "+" or elem == "-" or elem == "*" or elem == " ":
            arabic_expression += convert_roman_to_arabic(roman_number)
            arabic_expression += elem
            roman_number = ""
        elif elem == "/":
            arabic_expression += convert_roman_to_arabic(roman_number)
            arabic_expression += "//"
            roman_number = ""
        else:
            roman_number += elem

    arabic_expression += convert_roman_to_arabic(roman_number)  # add last number to the expression
    return arabic_expression


def convert_roman_to_arabic(roman_number: str) -> str:
    arabic_number = 0
    index = 0

    while index < len(roman_number):
        try:
            # parsing roman number is special type or not e.g. IV, IX, XL, XC, CD, CM
            arabic_number += numbers.number_repository[roman_number[index] + roman_number[index + 1]]
            index += 2
        except:
            arabic_number += numbers.number_repository[roman_number[index]]
            index += 1

    if arabic_number < 3999:
        return str(arabic_number)
    else:
        sys.exit("One or more input number is too large to display in roman number format!")


def get_calculated_expression(arabic_expression: str, roman_expression: str):
    arabic_result = eval(arabic_expression)
    if arabic_result < 3999:
        roman_result = convert_arabic_to_roman(str(arabic_result))
        return roman_expression + "=" + roman_result
    else:
        sys.exit("The end result is too large to display in roman number format!")

def convert_arabic_to_roman(arabic_number: str):
    roman_number = ""
    key_list = list(numbers.number_repository.keys())
    val_list = list(numbers.number_repository.values())

    for place_value in range(len(arabic_number)):
        value = int(arabic_number[place_value])
        number_pattern = str(value) + (len(arabic_number) - place_value - 1) * "0"

        try:
            position = val_list.index(int(number_pattern))
            roman_number += key_list[position]
        except ValueError:
            if value < 5:
                number_pattern = "1" + (len(arabic_number) - place_value - 1) * "0"
                position = val_list.index(int(number_pattern))
                roman_number += key_list[position] * value
            else:
                number_pattern = "5" + (len(arabic_number) - place_value - 1) * "0"
                position = val_list.index(int(number_pattern))
                roman_number += key_list[position]
                number_pattern = "1" + (len(arabic_number) - place_value - 1) * "0"
                position = val_list.index(int(number_pattern))
                roman_number += (key_list[position] * (value - 5))

    return roman_number
