from django import forms
from django.contrib.auth.models import User

class EstimationForm(forms.Form): #Extend ModelForm

		name        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Name','size':'48'}))		

		feat1        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quality'}))
		feat2        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Stakeholder Analysis'}))
		feat3        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Understanding Expectations'}))
		feat4        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Goal and Vision'}))
		feat5        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Leadership'}))
		
		feat6        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Team Cohesion'}))
		feat7        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Requirement Analysis'}))
		feat8        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Metric Estimation'}))
		feat9        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Planning'}))
		feat10       = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Risk Management'}))

		feat11       = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Software Architecture'}))
		feat12       = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Project Management'}))

	
