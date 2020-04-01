
""" Utility methods for working with strings """

def are_strings_anagrams(s1, s2):
    """ Decides if two strings contain the same letters,
    in any order. For example, 'book' and 'ookb' are anagrams.

    :param s1: the first string to compare
    :param s2: the second string to compare

    :returns: True if the strings are anagrams, False otherwise
    """
    return sorted(s1) == sorted(s2)


def reverse(s):
    """ Reverses the order of characters in a string
    
    :param s: the string to reverse
    
    :returns: a new string with the characters in reverse order
    """
    return s[::-1]