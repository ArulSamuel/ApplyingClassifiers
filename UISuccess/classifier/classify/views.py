# Create your views here.
from classify.forms import EstimationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from ClassificationLR import Project,Classifier

def HomePage(request):
		context={}
		return render_to_response('HomePage.html',context, context_instance=RequestContext(request))

def Result(request):
		context={}
		return render_to_response('ResultPage.html',context, context_instance=RequestContext(request))

def Train():
		classifier=Classifier()
		dataFileName="/home/arul/Git/SoftwareEnggPairResearch/UISuccess/classifier/classify/featData.txt";
		featFileName="/home/arul/Git/SoftwareEnggPairResearch/UISuccess/classifier/classify/featName.txt";
		projList=classifier.readData(featFileName,dataFileName)
		classifier.rate=0.01
		itera=3000
		classifier.trainData(projList,itera)
		#request.session['weights'] = classifier.weights
		return classifier

def Estimation(request):
		form=EstimationForm(request.POST)
		if request.method=='POST':  
				
				projName=str(form.data['name'])			
				feat={}
				feat["f1"]=float(form.data['feat1'])
				feat["f2"]=float(form.data['feat2'])
				feat["f3"]=float(form.data['feat3'])
				feat["f4"]=float(form.data['feat4'])
				feat["f5"]=float(form.data['feat5'])

				feat["f6"]=float(form.data['feat6'])
				feat["f7"]=float(form.data['feat7'])
				feat["f8"]=float(form.data['feat8'])
				feat["f9"]=float(form.data['feat9'])
				feat["f10"]=float(form.data['feat10'])

				feat["f11"]=float(form.data['feat11'])
				feat["f12"]=float(form.data['feat12'])
				print("Features",feat)
				
				classifier=Train()
				#weights=request.session['weights']
				#print("Weights",classifier.weights)
				pred=classifier.classify(feat)
				print("Value is ",pred)
				
				pred=round(pred,2)
				status=True
				if pred<0.65:
					status=False
				pred=pred*100
				context={'proj':projName,'status':status,'value':pred}
				return render_to_response('ResultPage.html',context, context_instance=RequestContext(request))

		else:    #Showing the form
				'''user is not submitting the form, show them a blank registration form'''
				form=EstimationForm()
				context={'form':form}
				return render_to_response('EstimationPage.html',context, context_instance=RequestContext(request))
