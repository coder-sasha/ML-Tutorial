"""
The function call counter
The output:

"""
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
        
    wrapper.calls = 0
    return wrapper

@count_calls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Zena")
   
print(f"'greet' was called {greet.calls} times.")
