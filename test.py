# write a function that takes a list of integers and returns the sum of all the integers in the list
def sum_list(lst):
    """
    Calculates the sum of all the elements in a given list.

    Parameters:
    lst (list): A list of numbers.

    Returns:
    int: The sum of all the elements in the list.
    """
    sum = 0
    for i in lst:
        sum += i
    return sum

# write a function that generates fibbonacci sequence up to n
def fibonacci(n):
    """
    Generates the Fibonacci sequence up to a given number n.

    Parameters:
    n (int): The number up to which the Fibonacci sequence should be generated.

    Returns:
    list: A list of Fibonacci numbers up to n.
    """
    fib = [0, 1]
    while fib[-1] + fib[-2] < n:
        fib.append(fib[-1] + fib[-2])
    return fib