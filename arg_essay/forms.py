from django import forms
from .models import *



class ThesisForm(forms.ModelForm):
	class Meta: 
		model = Thesis
		fields= ("declarative","support_one", "support_two", "support_three" )

class QuestionForm(forms.ModelForm):
	class Meta:
		model = userQuestion
		fields= ("question",)

class Tiqa_One_Form(forms.ModelForm):
	class Meta: 
		model = TiqaOne
		fields= ("topic_sentence_one", "intro_quote_one", "quote_one", "analysis_one_one", "analysis_one_two", )

class Tiqa_Two_Form(forms.ModelForm):
	class Meta: 
		model = TiqaTwo
		fields= ("topic_sentence_two", "intro_quote_two", "quote_two", "analysis_two_one", "analysis_two_two", )


class Tiqa_Three_Form(forms.ModelForm):
	class Meta: 
		model = TiqaThree
		fields= ("topic_sentence_three", "intro_quote_three", "quote_three", "analysis_three_one", "analysis_three_two", )







