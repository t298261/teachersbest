from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




def to_essay_question(request):
    return render(request, 'essay_question.html')

def to_claim(request):
    return render(request, 'claim.html')

def to_tiqa_one(request):
    return render(request, 'tiqa_one.html')

def to_tiqa_two(request):
    return render(request, 'tiqa_two.html')

def to_tiqa_three(request):
    return render(request, 'tiqa_three.html')

def to_essay_view(request):
    return render(request, 'essay_view.html')




def essayQuestion(request):
    form = userQuestion
    if request.method == 'POST':
        try:
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('claim-creator')
        except:
            None
    completed_form_ques = userQuestion.objects.filter(user=request.user)
    context = {'form': form, 'completed_form_ques': completed_form_ques}
    return render(request, 'essay_question.html', context)


def claim_creator(request, *arg):
    form = Thesis
    ques = userQuestion.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            form = ThesisForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('body-one')
        except:
            None
    completed_form_claim = Thesis.objects.filter(user=request.user)
    context = {'form': form, 'ques': ques, 'completed_form_claim': completed_form_claim}
    return render(request, 'claim.html', context)


def body_para_one(request, *arg):
    form = TiqaOne
    supp_all = Thesis.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            form = Tiqa_One_Form(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('body-two')
        except:
            None
    context = {'form': form, 'supp_all': supp_all}
    return render(request, 'tiqa_one.html', context)


def body_para_two(request, *arg):
    form = TiqaTwo
    supp_all = Thesis.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            form = Tiqa_Two_Form(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('body-three')
        except:
            None
    context = {'form': form, 'supp_all': supp_all}
    return render(request, 'tiqa_two.html', context)


def body_para_three(request, *arg):
    form = TiqaThree
    supp_all = Thesis.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            form = Tiqa_Three_Form(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('essay-v')
        except:
            None
    context = {'form': form, 'supp_all': supp_all}
    return render(request, 'tiqa_three.html', context)


def essay_view(request, *arg):
    complete_thesis = Thesis.objects.filter(user=request.user)
    tiqa_one = TiqaOne.objects.filter(user=request.user)
    tiqa_two = TiqaTwo.objects.filter(user=request.user)
    tiqa_three = TiqaThree.objects.filter(user=request.user)
    context = {'complete_thesis': complete_thesis, "tiqa_one": tiqa_one, "tiqa_two": tiqa_two, "tiqa_three": tiqa_three }
    return render(request, 'essay_view.html', context)



# def update_field(request, step_three):
# 	"""Form3 Edit post function"""
# 	step3 = StepThree.objects.filter(user=request.user)
# 	step_three = StepThree.objects.get(pk=step_three) #Needs to be a form completed by any user for this to work.
# 	form3 = StepThreeForm(instance=step_three)
# 	if request.method == 'POST':
# 		form3 = StepThreeForm(request.POST, instance=step_three)
# 		if form3.is_valid():
# 			form3.save()
# 			return redirect('user-homepage')
# 	return render(request,'update_form3.html', {"form3": form3, "step3": step3})


# def Step3_Form_Delete(request, step_three):
#     form = Thesis.objects.get(pk=step_three)
#     if request.method == "POST":
#     	form.delete()
#     	return redirect("user-homepage")
#     context = {'form': form}
#     return render(request, 'delete_form3.html', context)


