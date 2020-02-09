"""
lab7.py: Support count of combinations of top 6 frequent items
-uses lab 6 as a base
-calculates the support count of all items and makes a dictionary
-sorts the dictionary
-calculates what the top 6 items are
-calculates all combinations of the top 6
-calculates support counts of all combinations
"""

__author__ = "Matt Hunt"
__version__ = "1.0"
__date__ = "Oct 23 2019"

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


def combs_support_count(filename, all_combs):
    """
    takes the list of the top 6 combinations and finds the support count of every combination in the csv file
    :param filename: the csv file to be read
    :param all_combs: the list of all possible combinations of the top 6 most frequent items
    :return: combs_support, the dictionary of the support count of the frequent itemsets
    """
    combs_support = {}
    with open(filename) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            # for each row in the dataset
            for i in range(len(all_combs)):
                # loop through the all combinations list
                if set(all_combs[i]).issubset(set(row)) and all_combs[i] != ():
                    # if the combination is a subset of the row (in the row), dictionary entry created
                    if all_combs[i] in combs_support:
                        # if it already exists in the dictionary, increment 1
                        combs_support[all_combs[i]] += 1
                    else:
                        # if it doesn't exist in the dictionary, create entry with value of 1
                        combs_support[all_combs[i]] = 1
    return combs_support


if __name__ == '__main__':
    groceries_dict = reader('Groceries-CSCI4105-001.csv')
    freq = sort_dict_desc(groceries_dict)
    most_freq = get_top6(freq)
    grocery_combs = top6_combinations(most_freq)

    print("\nList of all combinations of the top 6 most frequent items:")
    for i in range(len(grocery_combs)):
        print("Itemset #" + str(i) + ":", grocery_combs[i])

    print(len(grocery_combs), "Total Combinations (including empty set)")
    print(len(grocery_combs) - 1, "Total Combinations (not including empty set)\n")

    combs_support_dict = combs_support_count('Groceries-CSCI4105-001.csv', grocery_combs)
    combs_support_dict_sorted = sort_dict_desc(combs_support_dict)

    print("Support Count for all combinations of the top 6 items:")
    for k, v in combs_support_dict_sorted:
        print(str(k) + ":", v)
