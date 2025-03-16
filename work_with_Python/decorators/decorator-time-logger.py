"""
This script is an example of using decorators to measure function execution time
The output:
Call of 'run_and_sleep()' took 2.015 sec
Processed 2 seconds of data.
Call of 'run_and_count()' took 0.372 sec
"""

import time


def log_time_decorator(func):
    def wrapper(*args, **kwargs): 
        start_time = time.perf_counter() 
        result = func(*args, **kwargs) 
        end_time = time.perf_counter()
        
        print(f"Call of '{func.__name__}()' took {end_time - start_time:.3f} sec")
        return result
        
    return wrapper


@log_time_decorator
def run_and_sleep(n):
    # imitate an execution delay
    time.sleep(n) 
    return f"Processed {n} seconds of data."


@log_time_decorator
def run_and_count():
    # execute a long counting loop: 10 mln multiplications
    for x in range(1, 10000000):
        r = ((x * 2) * 3) / x



print(run_and_sleep(2))
run_and_count()

 
