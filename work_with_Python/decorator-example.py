"""
This script demonstrates how to use a simple decorator
basic_decorator:
- kes the function as a parameter;
- d more functionality;
- turns function-parameter;

The output:
	+++ before the function call
	Hello Decorator!
+++ after the function call
+++ before the function call
	 No Message...
+++ after the function call
+++ before the function call
	 Python Decorators Are Power And Useful Tools
+++ after the function call
"""


def basic_decorator(func):
    def wrapper():
        print("+++ before the function call")
        func()
        print("+++ after the function call")

    return wrapper


@basic_decorator
def hello_function():
    print("\tHello Decorator!")


hello_function()


# an examples of a decorator for a function with arguments
def args_decorator(func):
    def wrapper(*args, **kwargs):
        print("+++ before the function call")
        func(*args, **kwargs)
        print("+++ after the function call")

    return wrapper


@args_decorator
def print_message(msg='no message...'):
    print('\t', msg.title())


print_message()
print_message("Python decorators are power and useful tools")
