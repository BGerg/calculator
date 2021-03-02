from calculator.cli.cli_parser import parse
from calculator.core.handle_data import *

def run(args):
    arabic_expression = convert_expression_to_arabic(args.roman_expression)
    result_expression = eval(arabic_expression)
    validate_roman_number(result_expression)
    print(f"{args.roman_expression} = {result_expression}")

if __name__ == "__main__":
    run(parse())