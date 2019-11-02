def factorial(n: int):
    """
    Returns the factorial of any number given
    params:
        -n (int)
    """
    if n==0:
        return 1
    return n * factorial(n - 1)


def binary_search(data, target: int, low: int, high: int):
    """
    Given a sorted data, algorithm finds a target position in O(logn)
    params:
        -data (iterable int)
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