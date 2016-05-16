_author_ = 'Marcus'
from data_merge import *

#filt uncessary attributes based on the siginificance analysis
def filter_data(data,attributes):
	for index in range(0,len(attributes)):
		attributes[index] -= index
	for cor_att in attributes:
		for row in data:
			del row[cor_att]
	return data


def write_csv(data):
	csvfile = file('2015-2016_del.csv','wb')
	writer = csv.writer(csvfile)
	writer = csv.writer(csvfile)
	for row in data:
		writer.writerow(row)
	csvfile.close()

def main():
	data,match_up = load_data()
	new_data = combine_data(data,match_up)
	attributes = [0,2,3,4,7,8,10,14,22,23,24,27,28,30,34]
	data_ = filter_data(new_data,attributes)
	write_csv(data_)
main()