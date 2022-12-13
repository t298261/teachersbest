from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.


# you have one to one here where every element links to one class: User so add one to one User relationship.
# so user object has one and only one questino claim etc. .  if it had many thesis's and question then you would use
# many to one one ot a Foreign Key, which is a many to one.


class argumentEssay(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    question = models.CharField(max_length=500, null=True)

    declarative = models.CharField(max_length=500, null=True)
    support_one = models.CharField(max_length=500, null=True)
    support_two = models.CharField(max_length=500, null=True)
    support_three = models.CharField(max_length=500, null=True)

    topic_sentence_one = models.CharField(max_length=500, null=True)
    intro_quote_one = models.CharField(max_length=500, null=True)
    quote_one = models.CharField(max_length=500, null=True)
    analysis_one_one = models.CharField(max_length=500, null=True)
    analysis_one_two = models.CharField(max_length=500, null=True)

    topic_sentence_two = models.CharField(max_length=500, null=True)
    intro_quote_two = models.CharField(max_length=500, null=True)
    quote_two = models.CharField(max_length=500, null=True)
    analysis_two_one = models.CharField(max_length=500, null=True)
    analysis_two_two = models.CharField(max_length=500, null=True)

    topic_sentence_three = models.CharField(max_length=500, null=True)
    intro_quote_three = models.CharField(max_length=500, null=True)
    quote_three = models.CharField(max_length=500, null=True)
    analysis_three_one = models.CharField(max_length=500, null=True)
    analysis_three_two = models.CharField(max_length=500, null=True)

    concl_intro = models.CharField(max_length=500, null=True)
    concl_recap_one = models.CharField(max_length=500, null=True)
    concl_recap_two = models.CharField(max_length=500, null=True)
    concl_recap_three = models.CharField(max_length=500, null=True)
    concl_ending = models.CharField(max_length=500, null=True)


    




   