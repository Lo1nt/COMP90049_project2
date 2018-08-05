import csv
import numpy as np




def readDataSet(path):
	with open(path, 'r') as trainSet:
		trainList = list(csv.reader(trainSet))
	return trainList

def process(dataList):
	data = list()
	
	for item in dataList:
		count = 0
		for amount in item[1:101]:
			count += int(amount)
		item.extend(str(count))
	return dataList


def main():

	dataList = readDataSet("dev_most100.csv")

	result = process(dataList)

	aMapping = dict()

	iniCount = list()

	for item in result:
		if item[102] not in iniCount:
			iniCount.append(item[102])
			aMapping[int(item[102])] = 0

	iniCount = np.array(iniCount)



	with open('predict_forest.txt', 'r') as forest:
		iCnt = 0
		for line in forest:
			if (result[iCnt][101] == line.strip('\n')):
				getCount = result[iCnt][102]
				aMapping[int(getCount)] += 1
			iCnt += 1;

	
	print aMapping		  




	

if __name__ == '__main__':
	main()


