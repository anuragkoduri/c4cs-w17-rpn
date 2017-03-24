#!/usr/bin/env python3

import operator
import readline
from termcolor import colored

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		##result = calculate(input('rpn calc> '))
		val = input('rpn calc> ')
		if val == '+':
			print(colored(val, 'red'))
		elif val == '-':
			print(colored(val, 'blue'))
		elif val == '*':
			print(colored(val, 'yellow'))
		elif val == '/':
			print(colored(val, 'green'))
		elif val == '*':
			print(colored(val, 'orange'))
		else:
			print(val)
		result = calculate(val)
		print("Result:", result)

if __name__ == '__main__':
	main()
