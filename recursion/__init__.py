def factorial(n: int):
    """
    Returns the factorial of any number given
    params:
        -n (int)
    time: O(n)
    """
    if n==0:
        return 1
    return n * factorial(n - 1)


def binary_search(data, target: int, low: int, high: int):
    """
    Given a sorted data, algorithm finds a target position in O(logn)
    params:
        -data (iterable int)
    time: O(log n)
    """
    # End search if interval empty; i.e match not found
    if low > high:
        return False
    mid = (low + high)//2
    mid_value = data[mid]
    if target == mid_value:
        return True
    elif target < mid_value:
        # recur to the left of the middle
        return binary_search(data, target, low, mid-1)
    else:
        # recur to the right of the middle
        return binary_search(data, target, mid+1, high)


def disk_usage(path):
    """
    Returns the total size of file/folder and any subfolder
    params:
        -path
    time: O(n)(amortization/tree traversal)
    """

    import os
    total = os.path.getsize(path)
    if os.path.isdir(path):
        # on my pc each folder is approximately 4kb excluding content
        total += 4096
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            # compute size of childpath/directory via recursion and sum with total
            total += disk_usage(childpath)
    return total

def fibonacci(n):
    """
    Returns pair of fibonacci number F(n), F(n-1)
    params:
        -n (int)
    time: O(n)
    """
    if n <= 1:
        return (0, n)
    (b, a) = fibonacci(n-1)
    return (a, a+b)

def change_max_recursion_depth(n=1000):
    """
    Changes the maximum recursion depth in python interpreter
    params:
        -n: (int) default is 1000
    returns:
        1: success
        -1: failed
    time: O(1)
    """
    import sys
    try:
        sys.setrecursionlimit(n)
        return 1
    except Exception:
        return -1

def linear_sum(S, n):
    """
    Returns the sum of the first n terms of sequence S
    params:
        - S (iterable)
        - n (int) stop position
    time: O(n)
    space: O(n)
    """
    if n<=0:
        return 0
    return linear_sum(S, n-1) + S[n-1]

def reverse(S, start, stop):
    """
    Reverse elements in a sequence slice
    params:
        - S (iterable)
        - start (int)
        - stop (int)
    time: O(n)
    """
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)
    return S

def power(x, n):
    """
    Returns the x**n
    params:
        - x (int)
        - n (int)
    time: O(n)
    """
    if n == 0:
        return 1
    return x * power(x, n-1)

def power_(x, n):
    """
    Returns the x**n
    k = n//2; when n is even: x^k**2 == x^n
              when n is odd: x^k**2 == x^n-1 == x.x^n
    params:
        - x (int)
        - n (int)
    time: O(log n)
    """
    if n == 0:
        return 1
    else:
        partial = power_(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        return result

def binary_sum(S, start, stop):
    """
    Returns sum of elements in a slice
    params:
        - S (iterable)
        - start (int)
        - stop (int)
    space: O(log n)
    time: O(n)
    """
    # no element in slice
    if start >= stop:
        return 0
    # one element in slice
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start+stop)//2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)