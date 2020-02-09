"""
lab6.py: csv reader and counting frequencies of data
"""

__author__ = "Matt Hunt"
__version__ = "1.0"
__date__ = "Oct 15 2019"

import csv
from more_itertools import powerset


def reader(filename):
    """
    Reads a csv file and returns a dictionary of the items
    :param filename: the csv file to be read
    :return: groceries, the dictionary of grocery items
    """
    groceries = {}
    with open(filename) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            # i is in range 2,17 because we are skipping the first two columns that only have the TID and names
            for i in range(2, 17):
                # skips the Items label and any blank spaces
                if row[i] != 'Items' and row[i] != '':
                    # if it is already in the dictionary value is increased by 1
                    if row[i] in groceries:
                        groceries[row[i]] += 1
                    else:
                        # create dictionary pair, starts at 1
                        groceries[row[i]] = 1
    return groceries


def sort_dict_desc(dictionary):
    """
    takes a dictionary and sorts it in descending order by the value
    :param dictionary: the dictionary to be sorted
    :return: the sorted dictionary that shows the items and their frequencies sorted by the frequencies
    """
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def get_top6(sorted_dict):
    """
    find the top 6 most frequent items in the sorted grocery dictionary
    :param sorted_dict: the sorted dictionary input
    :return: top6, set of top 6 items
    """
    top6 = set()
    for i in range(6):
        top6.add(sorted_dict[i][0])
    return top6


def top6_combinations(top6_set):
    """
    Creates the list of all combinations possible of the top 6 most frequent items
    :param top6_set: the set of the 6 most frequent items
    :return: the list of all combinations of the top 6 items possible
    """

    # uses the powerset function from itertools
    # returns list of all combinations of an iterable object
    all_combs = []
    for itemset in powerset(top6_set):
        all_combs.append(itemset)
    return all_combs


if __name__ == '__main__':
    groceries_dict = reader('Groceries-CSCI4105-001.csv')
    print("Unique Items:")
    for items in sorted(groceries_dict.keys()):
        print(items)

    freq = sort_dict_desc(groceries_dict)
    print("\nUnique Items and their frequencies:")
    for item in freq:
        print(item)

    most_freq = get_top6(freq)
    print("\nTop 6 most frequent items:")
    print(most_freq)

    grocery_combs = top6_combinations(most_freq)
    print("\nList of all combinations of the top 6 most frequent items:")
    for i in range(len(grocery_combs)):
        print("Itemset #" + str(i) + ":", grocery_combs[i])

    print(len(grocery_combs), "Total Combinations (including empty set)")
    print(len(grocery_combs) - 1, "Total Combinations (not including empty set)")
