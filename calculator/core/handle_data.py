from calculator.core.numbers import number_repository

from calculator.core.too_large_to_convert_error import TooLargeToConvertError


def convert_expression_to_arabic(roman_expression: str):
    roman_number = ""
    arabic_expression = ""
    stripped_expression = [e.strip(" ") for e in roman_expression]

    for elem in stripped_expression:
        if elem == "+" or elem == "-" or elem == "*":
            arabic_expression += convert_roman_to_arabic(roman_number) + elem
            roman_number = ""
        elif elem == "/":
            arabic_expression += convert_roman_to_arabic(roman_number) + "//"
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
            arabic_number += number_repository[roman_number[index] + roman_number[index + 1]]
            index += 2
        except (KeyError, IndexError):
            arabic_number += number_repository[roman_number[index]]
            index += 1

    return str(arabic_number)

def validate_roman_number(number: int):
    if number < 3999:
        raise TooLargeToConvertError("The end result is too large to display in roman number format!")


def convert_arabic_to_roman(arabic_number: str):
    roman_number = ""
    roman_repo = {value: key for key, value in number_repository.items()}

    for place_value in range(len(arabic_number)):
        value = int(arabic_number[place_value])

        _get_decimal = lambda value_: value_ * 10 ** (len(arabic_number) - place_value - 1)

        try:
            roman_number += roman_repo[_get_decimal(value)]
        except KeyError:
            # repeat character 'value' times
            if value < 5:
                roman_number += roman_repo[_get_decimal(1)] * value
            else:
                roman_number += roman_repo[_get_decimal(5)]
                roman_number += (roman_repo[_get_decimal(1)] * (value - 5))

    return roman_number
