def factorial(n: int):
    """
    Returns the factorial of any number given
    params:
        -n (int)
    """
    if n==0:
        return 1
    return n * (n - 1)
