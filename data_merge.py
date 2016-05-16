_author_ = 'Marcus'
from numpy import *
import csv
# load the data
def load_data():
    # load data and split the match up attribute 
    data = genfromtxt('2015_2016 FORMER.csv', dtype = None , delimiter=',')
    attri = []
    for row in range(0,data.shape[0]):
    	attri.append(data[row,1].split())
    data = data.tolist()
    return data,attri

# combine two teams stats at the same match in one row
def combine_data(data,match_up):
	new_data = []
	for row_1 in range(1,len(data)): 
		new_row = []
		for row_2 in range(row_1 + 1,len(data)):
			if match_up[row_1][0] == match_up[row_2][2] and data[row_1][2] == data[row_2][2]:
				new_row.extend(data[row_1][2:])
				new_row.extend(data[row_2][4:])
				if match_up[row_1][1] == '@':
					new_row.append('yes')
				else:
					new_row.append('no')
		if new_row:
			new_data.append(new_row)
 	return new_data


def write_csv(data):
	csvfile = file('2015-2016.csv','wb')
	writer = csv.writer(csvfile)
	for row in data:
		writer.writerow(row)
	csvfile.close()


def main():
	data,match_up = load_data()
	new_data = combine_data(data,match_up)
	write_csv(new_data)
main()






