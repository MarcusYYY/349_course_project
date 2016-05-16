_author_ = 'Marcus'
import csv
from numpy import *
from data_merge import *
from math import *

def check_error(data_1,data_2):
	len_1 = 1 
	len_2 = 0
	error_date = []
	while len_1 < len(data_1) and len_2 < len(data_2):
		if data_1[len_1][2] != data_2[len_2][0]:
			error_date.append(len_1)
			len_2 -= 1
		len_1 += 1
		len_2 += 1
	return error_date


def load_data():
    # load data and split the match up attribute 
    data_1 = genfromtxt('2015_2016 FORMER.csv', dtype = None , delimiter=',')
    data_2 = genfromtxt('2015-2016.csv', dtype = None , delimiter=',')
    data_1 = data_1.tolist()
    data_2 = data_2.tolist()
    return data_1,data_2

def main():
	data_1,data_2 = load_data()
	error_data = check_error(data_1,data_2)
	print error_data
main()
