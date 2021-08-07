import os
import csv
import numpy as np


csvpath = "Resources\\budget_data.csv"
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)