import argparse


def parse():
    parser = argparse.ArgumentParser(description='Calculate mathematical expression in roman number format.'
                                                 'The application works with maximum value 3999.',
                                     epilog='All way lead to rom :)')

    parser.add_argument('roman_expression',
                        metavar='Roman expression',
                        type=str,
                        help='Needs a math expression with roman numbers e.g. I+IV*2 ')



    return parser.parse_args()
