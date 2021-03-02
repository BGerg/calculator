import unittest
from calculator.core.handle_data import *


class MyTestCase(unittest.TestCase):

    def test_convert_roman_to_arabic(self):
        self.assertEqual(convert_roman_to_arabic("I"), "1")
        self.assertEqual(convert_roman_to_arabic("II"), "2")
        self.assertEqual(convert_roman_to_arabic("III"), "3")
        self.assertEqual(convert_roman_to_arabic("IV"), "4")
        self.assertEqual(convert_roman_to_arabic("V"), "5")
        self.assertEqual(convert_roman_to_arabic("VI"), "6")
        self.assertEqual(convert_roman_to_arabic("VII"), "7")
        self.assertEqual(convert_roman_to_arabic("VIII"), "8")
        self.assertEqual(convert_roman_to_arabic("IX"), "9")
        self.assertEqual(convert_roman_to_arabic("X"), "10")
        self.assertEqual(convert_roman_to_arabic("XXX"), "30")
        self.assertEqual(convert_roman_to_arabic("LX"), "60")
        self.assertEqual(convert_roman_to_arabic("XC"), "90")
        self.assertEqual(convert_roman_to_arabic("CD"), "400")
        self.assertEqual(convert_roman_to_arabic("CM"), "900")
        self.assertEqual(convert_roman_to_arabic("MDCCCLXXXVI"), "1886")
        self.assertEqual(convert_roman_to_arabic("MCXI"), "1111")
        self.assertEqual(convert_roman_to_arabic("MCMXCIX"), "1999")
        self.assertEqual(convert_roman_to_arabic("XIV"), "14")
        # with self.assertRaises(TooLargeToConvertError):
        #     convert_roman_to_arabic("MMMM")

    def test_convert_expression_to_arabic(self):
        self.assertEqual("1+1", convert_expression_to_arabic("I+I"))
        self.assertEqual(convert_expression_to_arabic("I+II"), "1+2")
        self.assertEqual(convert_expression_to_arabic("I+IV"), "1+4")
        self.assertEqual(convert_expression_to_arabic("I+IV+I"), "1+4+1")
        self.assertEqual(convert_expression_to_arabic("I+M+I+C"), "1+1000+1+100")
        self.assertEqual(convert_expression_to_arabic("I-IV"), "1-4")
        self.assertEqual(convert_expression_to_arabic("I+IV-X"), "1+4-10")
        self.assertEqual(convert_expression_to_arabic("I+M-I+C"), "1+1000-1+100")
        self.assertEqual(convert_expression_to_arabic("I*IV"), "1*4")
        self.assertEqual(convert_expression_to_arabic("I*IV/IX-II+I"), "1*4//9-2+1")
        self.assertEqual(convert_expression_to_arabic("I*VI"), "1*6")
        self.assertEqual(convert_expression_to_arabic("I*DC"), "1*600")

    def test_get_calculated_expression(self):
        self.assertEqual(2, eval(convert_expression_to_arabic("I+I")))
        self.assertEqual(3, eval(convert_expression_to_arabic("I+II")))
        self.assertEqual(5, eval(convert_expression_to_arabic("I+IV")))

    def test_convert_arabic_to_roman(self):
        self.assertEqual(convert_arabic_to_roman("611"), "DCXI")
        self.assertEqual(convert_arabic_to_roman("3999"), "MMMCMXCIX")
        self.assertEqual(convert_arabic_to_roman("6"), "VI")
        self.assertEqual(convert_arabic_to_roman("768"), "DCCLXVIII")
        self.assertEqual(convert_arabic_to_roman("968"), "CMLXVIII")
