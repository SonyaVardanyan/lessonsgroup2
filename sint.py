#!/usr/bin/python3
def is_valid_expression(expression):
    try:
        eval(expression)
        return True
    except SyntaxError:
        return False

# Example usage
user_input = input("Enter a mathematical expression: ")
if is_valid_expression(user_input):
    print(True)
else:
    print(False)
