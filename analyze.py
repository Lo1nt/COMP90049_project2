
import csv
import sys
import time
import numpy as np
from sklearn import svm
from sklearn import tree
from sklearn import neighbors
from sklearn import metrics
from sklearn import naive_bayes
from sklearn import ensemble

def readDataSet(path):
	with open(path, 'r') as trainSet:
		trainList = list(csv.reader(trainSet))
	return trainList

def getData(dataList):
	data = list()
	for item in dataList:
		data.append(item[1:101])
	dataSet = np.array(data)
	return dataSet

def getLabel(dataList):
	label = list()
	for item in dataList:
		label.append(item[101])
	labelSet = np.array(label)
	return labelSet


def bayesEvaluation(train, label, test):
	model = naive_bayes.MultinomialNB()
	return timeingPredict(train, label, test, model, "bayes")

def forestEvaluation(train, label, test):
	model = ensemble.RandomForestClassifier()
	return timeingPredict(train, label, test, model, "forest")

def svmEvaluation(train, label, test):
	model = svm.SVC()
	return timeingPredict(train, label, test, model, "svm")


def treeEvaluation(train, label, test):
	model = tree.DecisionTreeClassifier()
	return timeingPredict(train, label, test, model, "dTree")

def knnEvaluation(train, label, test):
	model = neighbors.KNeighborsClassifier(n_neighbors = 3, algorithm="auto")
	return timeingPredict(train, label, test, model, "knn")

def timeingPredict(train, label, test, model, method):
	begin = time.time()

	model.fit(train, label)
	trainTimePause = time.time()
	print(method + " model establishment time: " + str(trainTimePause - begin) + "s")
	predict = model.predict(test)
	predictTimePause = time.time()
	print(method + " model prediction time: " + str(predictTimePause - trainTimePause) + "s")

	path = "predict_" + method + ".txt"
	with open(path, 'w') as out:
		for item in predict:
			out.write(predict)
			out.write('\n')
	return predict

def evaluate(target, predict, method):
	report = metrics.classification_report(target, predict)
	print report
	path = 'out_' + str(method) + ".txt"
	with open(path, 'w') as out:
		out.write(report)

def main():
	trainPath = sys.argv[1]
	testPath = sys.argv[2]
	method = sys.argv[3]

	trainList = readDataSet(trainPath)
	testList = readDataSet(testPath)

	trainSet = getData(trainList)
	labelSet = getLabel(trainList)
	testSet = getData(testList)
	testLabel = getLabel(testList)

	if (method == 'svm'):
		predict = svmEvaluation(trainSet, labelSet, testSet)
	elif (method == 'tree'):
		predict = treeEvaluation(trainSet, labelSet, testSet)
	elif (method == 'knn'):
		predict = knnEvaluation(trainSet, labelSet, testSet)
	elif (method == 'bayes'):
		predict = bayesEvaluation(trainSet, labelSet, testSet)
	elif (method == 'forest'):
		predict = forestEvaluation(trainSet, labelSet, testSet)
	
	evaluate(testLabel, predict, method)

if __name__ == '__main__':
	main()







