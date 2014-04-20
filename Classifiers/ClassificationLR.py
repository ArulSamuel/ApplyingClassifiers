import math

class Project:
	projName=""
	features={}
	label=""
	def __init__(self,projName,features,label):
		self.projName=projName
		self.features=features
		self.label=label


class Classifier:
	
	def __init__(self):
		# self.rate -> Learning Rate 
		self.rate=0.01
		self.weights={}
		return

	def readData(self,dataFileName):
		f=open(dataFileName,'rU')
		noOfFeat=int(f.readline())
		print 'Number of Features are ',noOfFeat
		
		i=0
		featNames=[]
		projList=[]
		for line in f:
			if i<noOfFeat:
				featNames.append(line)
				i=i+1
			else:
				feat={}
				if(line!="\n"):
					list1=line.split()
					feat["f1"]=float(list1[1])
					feat["f2"]=float(list1[2])
					feat["f3"]=float(list1[3])
					proj=Project(list1[0],feat,float(list1[4]))
					print proj.projName,proj.label
					projList.append((proj.features,proj.label))
		print 'Project List Size is ',len(projList)
		return projList

	def trainData(self,projList, noOfIter):
	    for i in range(noOfIter):
		for feat,label in projList:
			predictedLabel=self.classify(feat)
			print ' ',predictedLabel,' ',label
			for ft,value in feat.iteritems():
				if ft not in self.weights:
					self.weights[ft]=0.0
				update=(label-predictedLabel)*value
				self.weights[ft]=self.weights[ft]+self.rate*update
		print 'Iteration ',i,' Done'
		print 'Weights are ',self.weights
	     
	
	def classify(self, features):
		predictedVal=0.0
		weightVal=0.0
		for ft,value in features.iteritems():
			if ft in self.weights:
				weightVal=self.weights[ft]
			predictedVal += weightVal * value  
		return 1.0/(1.0 + math.exp(-predictedVal))


if __name__ == "__main__":
	classifier=Classifier()
	dataFileName="ProjectData.txt";
	projList=classifier.readData(dataFileName)
	classifier.rate=0.01
	itera=5000
	classifier.trainData(projList,itera)
