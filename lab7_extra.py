"""
lab7_extra.py: Implementing the Apriori Algorithm
"""

__author__ = "Matt Hunt"
__version__ = "1.0"
__date__ = "Oct 24 2019"

import csv
from apyori import apriori


def get_transactions(filename):
    """
    scans the dataset and creates a list of lists of the transactions
    :param filename: the csv file that contains the transactions to scan through
    :return: the transactions list
    """
    transactions = []
    temp = []
    with open(filename) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            for i in range(2, len(row)):
                if row[i] != "Items" and row[i] != "":
                    # adds row to a temp list
                    temp.append(row[i])
            # temp list added to transactions list of lists
            transactions.append(temp)
            # temp list reset to empty
            temp = []
        # removes blank list from first index
        transactions.remove(transactions[0])

    return transactions


def create_rules(transactions, min_s, min_c, min_l):
    """
    Uses the apriori algorithm to create interesting rules
    :param transactions: the list of transactions from the csv file
    :param min_s: the minimum support
    :param min_c: the minimum confidence
    :param min_l: the minimum length of the rules
    :return: the list of created rules
    """
    rules = apriori(transactions, min_support=min_s, min_confidence=min_c, min_length=min_l)
    rules_list = list(rules)

    return rules_list


def print_rules(rules_list):
    """
    takes the list of created rules and prints them in a more readable form
    :param rules_list: the created rules from the apriori algorithm
    """
    r = []
    temp = []
    for items in rules_list:
        # set that is the first part of the rule
        tempset = set(items[2][0][0])
        # added to temp list
        temp.append(tempset)
        # set that is the second part of the rule
        tempset = set(items[2][0][1])
        # added to temp list
        temp.append(tempset)
        # support added to temp list
        temp.append(items[1])
        # confidence added to temp list
        temp.append(items[2][0][2])

        # all parts of rule in temp list added to final list r
        r.append(temp)
        # temp list reset
        temp = []

    num = 1
    # print all parts of r in a more readable way
    for r1, r2, s, c in r:
        print("Rule #" + str(num) + ":", r1, "-->", r2)
        print("Support:", "{:.2}".format(s))
        print("Confidence:", "{:.2}".format(c), "\n")
        num += 1


if __name__ == '__main__':
    dataset = get_transactions("Groceries-CSCI4105-001.csv")
    print("All transactions in csv file:")
    for i in range(len(dataset)):
        print("Transaction #" + str(i + 1), dataset[i])

    sup = 0.15
    conf = 0.60
    min_len = 2
    apriori_rules = create_rules(dataset, sup, conf, min_len)

    print("\nRules created using Apriori Algorithm with min support of", sup, "and min confidence of", conf)
    print_rules(apriori_rules)
