""" Utility methods for working with lists and dictionaries """


def merge_dicts(d1, d2):
    """
     Combines the entries of two dictionaries to make another dictionary.

    :param d1: the first dictionary 
    :param d2: the second dictionary

    :returns: a dictionary created from the entries of d1 and the entries of d2 
    """
    return {**d1, **d2}


def merge_lists(l1, l2):

    """ Combines the elements of two lists to make another list.

    :param l1: the first list 
    :param l2: the scond list 

    :returns: a list created from the elements of l1 followed by the elements of l2 
    """
    return [ *l1, *l2 ]


def make_dict(keys, values):
    """
    Creates a new dictionary by pairing the items in the first sequence with 
    items in the second sequence.

    :param keys: a sequence of keys 
    :param values: a sequence of values 
    
    :returns: a dictionary built from the keys and values sequences
    """

    return dict(zip(keys, values))



