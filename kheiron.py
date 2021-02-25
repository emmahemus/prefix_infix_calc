

def calculate_prefix(prefix):
    # removing spaces and tokenizing
    tokens = prefix.split(" ")

    # removing any empty strings (would occur if multiple spaces)
    prefix_tokens = []
    for t in tokens:
        if t == "":
            pass
        else:
            prefix_tokens.append(t)

    # calling recursive parse_prefix function
    return parse_prefix(prefix_tokens)


def parse_prefix(tokens):
    token = tokens.pop(0)
    if token == "+":
        return int(parse_prefix(tokens) + parse_prefix(tokens))
    elif token == "-":
        return int(parse_prefix(tokens) - parse_prefix(tokens))
    elif token == "*":
        return int(parse_prefix(tokens) * parse_prefix(tokens))
    elif token == "/":
        return int(parse_prefix(tokens) / parse_prefix(tokens))
    else:
        if token.isdigit():
            return int(token)
        else:
            raise ValueError("Invalid token: " + token)


def perform_operation(op, num1, num2):
    # checking for type errors
    if not isinstance(op, str):
        raise TypeError("operator is not a string")
    if not isinstance(num1, int):
        raise TypeError("num1 is not an integer")
    if not isinstance(num2, int):
        raise TypeError("num2 is not an integer")

    # performing operations
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid maths operator: " + op)


def validity_check(tokens, digits):
    right_p = tokens.count("(")
    left_p = tokens.count(")")
    ops = tokens.count("+") + tokens.count("-") + tokens.count("*") + tokens.count("/")

    # checking parentheses
    if right_p != left_p:
        raise ValueError("Input is not fully parenthesized")

    # case with no operator and one number
    elif ops == 0 and len(digits) == 1:
        return True

    # there are either too many operators or empty parentheses
    elif right_p != ops:
        raise ValueError("Invalid calculation")

    else:
        return True


def calculate_infix(infix):
    # removing spaces and tokenizing
    tokens = infix.split(" ")

    # removing any empty strings (would occur if multiple spaces)
    infix_tokens = []
    for t in tokens:
        if t == "":
            pass
        else:
            infix_tokens.append(t)

    # digits will contain any numbers in the input
    digits = [n for n in tokens if n.isdigit()]

    # calling function to check for some potential input errors
    if validity_check(tokens, digits):

        if len(digits) == 1:
            # the infix must be a single number
            return int(digits[0])

        # validity checks have passed and there is at least one operation
        else:
            operators = []
            numbers = []

            op_list = "(+-*/"

            for char in tokens:
                # collecting all operators as defined in op_list
                if char in op_list:
                    operators.append(char)

                # collecting all numbers
                elif char.isdigit():
                    numbers.append(char)

                # if char is not a number or in op_list, it must be ')'.
                # this signifies it is time to perform a maths operation
                else:
                    # pops off maths operator
                    op = operators.pop()
                    # pops off the two numbers for the operation
                    num2 = int(numbers.pop())
                    num1 = int(numbers.pop())

                    # perform maths operation
                    numbers.append(perform_operation(op, num1, num2))

                    # pop off '('
                    operators.pop()

            return numbers[0]

