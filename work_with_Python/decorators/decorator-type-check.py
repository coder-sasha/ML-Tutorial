"""
The example of using decorators for arguments type checking
The output:
5
Traceback (most recent call last):
  File "C:\aWork\bin25\CG-ML\my_ml\work_with_python\decorators\decorator-type-check.py", line 25, in <module>
    print(add('two', 'three'))
  File "C:\aWork\bin25\CG-ML\my_ml\work_with_python\decorators\decorator-type-check.py", line 10, in wrapper
    raise TypeError(f"Expected {expected}, got {type(arg)}")
TypeError: Expected <class 'int'>, got <class 'str'>
"""


def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected}, got {type(arg)}")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int, int)
def add(a, b):
    return a + b


# usage
print(add(2, 3))
# this throws an exception
print(add('two', 'three'))
