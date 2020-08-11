#!/usr/bin/python3
"""Function that return the minimum operation"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    suma = 0
    if type(n) is not int or n < 2:
        return suma
    i = 2
    while i <= n:
        if n % i == 0:
            suma += i
            n = n // i
        else:
            i += 1
    return suma
