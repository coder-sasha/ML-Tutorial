"""
The example of using decorators for function call debugging.
The output:
Calling 'run_multiplication' with args: (2, 2) kwargs: {}
'run_multiplication' returns: 4
2 * 2=4
Calling 'run_multiplication' with args: (6, 6) kwargs: {}
'run_multiplication' returns: 36
6 * 6=36
Calling 'run_multiplication' with args: (21, 2) kwargs: {}
'run_multiplication' returns: 42
21 * 2=42
"""


def dec_debug(func):
	def wrapper(*args, **kwargs):
		print(f"Calling '{func.__name__}' with args: {args} kwargs: {kwargs}")
		result = func(*args, **kwargs)
		print(f"'{func.__name__}' returns: {result}")
		return result

	return wrapper


@dec_debug
def run_multiplication(a, b):
	return a * b
	

# usage
print(f"2 * 2={run_multiplication(2, 2)}")
print(f"6 * 6={run_multiplication(6, 6)}")
print(f"21 * 2={run_multiplication(21, 2)}")
