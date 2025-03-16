"""
This generator example yields an approximations of the square root of a number using the Newton-Raphson method. 
This can be useful when you need a series of approximations to decide when to stop or to monitor convergence.
"""

def sqrt_newton_gen(x: float, tolerance: float=1e-10)->float:
    """
    Yields successive approximations to the square root of x using the Newton-Raphson method.
    
    :param x: The number to compute the square root of.
    :param tolerance: The stopping criteria based on the squared difference.
    :yield: An approximation of sqrt(x).
    """
    # initial guess of result
    guess = x / 2.0  
    while True:
        yield guess
        new_guess = (guess + x / guess) / 2.0
        if abs(new_guess - guess) < tolerance:
            yield new_guess
            break
            
        guess = new_guess

# usage
if __name__ == '__main__':
    x = 25.0
    approximations = sqrt_newton_gen(x)
    for approx in approximations:
        print(f"Approximation: {approx}")