import unittest
from kheiron import calculate_prefix, perform_operation, calculate_infix


class CalculatePrefix(unittest.TestCase):
    def test_single_digit_space(self):
        result = calculate_prefix(" 3")
        self.assertEqual(result, 3)

    def test_single_digit(self):
        result = calculate_prefix("3")
        self.assertEqual(result, 3)

    def test_add_space(self):
        result = calculate_prefix(" + 1 2 ")
        self.assertEqual(result, 3)

    def test_add(self):
        result = calculate_prefix("+ 1 2")
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = calculate_prefix("- 0 3")
        self.assertEqual(result, -3)

    def test_multiply(self):
        result = calculate_prefix("* 1 2")
        self.assertEqual(result, 2)

    def test_divide(self):
        result = calculate_prefix("/ 3 2")
        self.assertEqual(result, 1)

    def test_add_multiply(self):
        result = calculate_prefix("+ * 1 2 3")
        self.assertEqual(result, 5)

    def test_subtract_divide_add_multiply(self):
        result = calculate_prefix("- / 10 + 1 1 * 1 2")
        self.assertEqual(result, 3)

    def test_value_error(self):
        self.assertRaises(ValueError, calculate_prefix, "3+")

    # this test is for invalid inputs. ideally a function would filter these out
    def test_invalid_input(self):
        result = calculate_prefix("* * 1 2")
        self.assertEqual(result, 2)


class TestPerformOp(unittest.TestCase):
    def test_simple_add(self):
        result = perform_operation("+", 2, 3)
        self.assertEqual(result, 5)

    def test_simple_subtract(self):
        result = perform_operation("-", 8, 3)
        self.assertEqual(result, 5)

    def test_simple_multiply(self):
        result = perform_operation("*", 5, 1)
        self.assertEqual(result, 5)

    def test_simple_divide(self):
        result = perform_operation("/", 10, 2)
        self.assertEqual(result, 5)

    def test_negative_add(self):
        result = perform_operation("+", -2, 7)
        self.assertEqual(result, 5)

    def test_negative_subtract(self):
        result = perform_operation("-", 3, -2)
        self.assertEqual(result, 5)

    def test_negative_multiple(self):
        result = perform_operation("*", -1, -5)
        self.assertEqual(result, 5)

    def test_negative_divide(self):
        result = perform_operation("/", -10, -2)
        self.assertEqual(result, 5)

    def test_large_add(self):
        result = perform_operation("+", 2**30, 1)
        self.assertEqual(result, (2**30 + 1))

    def test_large_subtract(self):
        result = perform_operation("-", 2**30, 1)
        self.assertEqual(result, (2**30 - 1))

    def test_large_multiply(self):
        result = perform_operation("*", 2**30, 1)
        self.assertEqual(result, 2**30)

    def test_large_divide(self):
        result = perform_operation("/", 2**30, 1)
        self.assertEqual(result, 2**30)

    def test_type_error_num(self):
        self.assertRaises(TypeError, perform_operation, "+", 2, "3")

    def test_type_error_op(self):
        self.assertRaises(TypeError, perform_operation, 5, 2, 3)

    def test_value_error(self):
        self.assertRaises(ValueError, perform_operation, "(", 2, 3)

    def test_zero_add(self):
        result = perform_operation("+", 5, 0)
        self.assertEqual(result, 5)

    def test_zero_subtract(self):
        result = perform_operation("-", 5, 0)
        self.assertEqual(result, 5)

    def test_zero_multiply(self):
        result = perform_operation("*", 5, 0)
        self.assertEqual(result, 0)

    def test_zero_divide(self):
        self.assertRaises(ZeroDivisionError, perform_operation, "/", 2, 0)


class CalculateInfix(unittest.TestCase):
    def test_one_calc(self):
        result = calculate_infix("( 1 + 2 )")
        self.assertEqual(result, 3)

    def test_add_one_calc(self):
        result = calculate_infix("( 1 + ( 2 * 3 ) )")
        self.assertEqual(result, 7)

    def test_one_calc_add(self):
        result = calculate_infix("( ( 1 * 2 ) + 3 )")
        self.assertEqual(result, 5)

    def test_two_calc_divide_subtract(self):
        result = calculate_infix(" ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )")
        self.assertEqual(result, (-2))

    def test_two_calc_multiply(self):
        result = calculate_infix(" ( ( 4 - 3 ) * ( 5 - 4 ) )")
        self.assertEqual(result, 1)

    def test_number_only(self):
        result = calculate_infix(" ( 56 )")
        self.assertEqual(result, 56)

    def test_no_numbers(self):
        self.assertRaises(ValueError, calculate_infix, " ( ) ")

    def test_value_error_operator(self):
        self.assertRaises(ValueError, calculate_infix, " ( + ( 5 - 4 ) + )")

    def test_value_error_parentheses_mismatch(self):
        self.assertRaises(ValueError, calculate_infix, " ( 1 + 1 ) )")

    def test_value_error_parentheses_empty(self):
        self.assertRaises(ValueError, calculate_infix, " ( ( 4 - 3 ) ( )")


if  __name__ == "__main__":
    unittest.main()