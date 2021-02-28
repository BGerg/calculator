from calculator.cli.cli_parser import parse
from calculator.core.handle_data import *

def handle(args):
    arabic_expression = convert_expression_to_arabic(args.roman_expression)
    result_expression = get_calculated_expression(arabic_expression, args.roman_expression)
    print(result_expression)

if __name__ == "__main__":
    handle(parse())