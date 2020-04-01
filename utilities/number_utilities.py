""" Utility methods for working with numbers """

def is_number_in_range(n, low, high):

    """
    Identifies if a number is within a range, including the 
    low and high values of the range. 

    :param n: the number to test
    :param low: the low or min value of the range
    :param high: the high or max value of the range 

    :returns: True if the number n is between low and high, including low and high 

    """
    return low <= n <= high

