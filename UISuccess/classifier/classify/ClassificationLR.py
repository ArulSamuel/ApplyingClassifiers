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

	def readData(self,featFileName,dataFileName):
		f1=open(featFileName,'rU')		
		featNames=[]
				
		for line in f1:
			featNames.append(str(line))
		
		noOffeat=len(featNames)		
		f=open(dataFileName,'rU')

		#noOfFeat=int(f.readline())
		print 'Number of Features are ',noOffeat
		
		i=0
		projList=[]
		for line in f:
			feat={}
			if(line!="\n"):
				list1=line.split(':')
				feat["f1"]=float(list1[1])
				feat["f2"]=float(list1[2])
				feat["f3"]=float(list1[3])
				feat["f4"]=float(list1[4])
				feat["f5"]=float(list1[5])
				feat["f6"]=float(list1[6])
				feat["f7"]=float(list1[7])
				feat["f8"]=float(list1[8])
				feat["f9"]=float(list1[9])
				feat["f10"]=float(list1[10])
				feat["f11"]=float(list1[11])
				feat["f12"]=float(list1[12])
														
				proj=Project(list1[0],feat,float(list1[13]))
				print proj.projName,proj.label
				projList.append((proj.features,proj.label))
		print 'Project List Size is ',len(projList)
		return projList

	def trainData(self,projList, noOfIter):
	    for i in range(noOfIter):
		for feat,label in projList:
			predictedLabel=self.classify(feat)
			print '-',predictedLabel,' ',label
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
	dataFileName="featData.txt";
	featFileName="featName.txt";
	projList=classifier.readData(featFileName,dataFileName)
	classifier.rate=0.01
	itera=500
	classifier.trainData(projList,itera)
