""" A file that demonstrates using some utilities """

from utilities import collection_utilities, string_utilities, number_utilities

def main():

    """ A main method that calls various utility functions and prints the output """

    # Merging two dictionaries 

    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}

    print(collection_utilities.merge_dicts(d1, d2))  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Merge two lists 

    l1 = [1, 2, 3]
    l2 = [100, 200, 300]
    print(collection_utilities.merge_lists(l1, l2))  # [1, 2, 3, 100, 200, 300]


    # Make a dictionary from two lists, one of keys, one of values 
    things = ['computer', 'pencil', 'book']
    verbs = ['type', 'write', 'read']

    print(collection_utilities.make_dict(things, verbs))


    # Are two strings anagrams of each other?

    print(string_utilities.are_strings_anagrams('cat', 'dog'))  # False
    print(string_utilities.are_strings_anagrams('cat', 'act'))  # True


    # Is a number between two other numbers?

    print(number_utilities.is_number_in_range(10, 0, 100))   # True
    print(number_utilities.is_number_in_range(-1, 0, 100))   # False


if __name__ == '__main__':
    main()