# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:33:48 2019

@author: Oleg
"""

import csv


def csv_dict_reader(file_obj, data = [], cost = []):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        data.append(line["Дата"]),
        cost.append(line["Расход"])

if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_dict_reader(f_obj, data, cost)
        print(data)
        print(cost)