from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Questions
from copo.form import *


def func_main(request):
    if request.user.is_authenticated:
        print(request.user.username)
        if request.method == "POST":
            new_question = Questions(title=request.POST['title'], description=request.POST['description'],
                                     test=request.FILES['test'])
            new_question.save()
            # form = QuestionForm(request.POST)
            # if form.is_valid():
            #     form.save()
            return redirect('main')
        else:
            all_questions = Questions.objects.all()
            return render(request, 'index.html',
                          {'path': request.get_host(), 'all_questions': all_questions, 'user': request.user.username,
                           'email': request.user.email})
    else:
        return redirect('accounts/login/')


def func_login(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('/')
    return render(request, 'Login.html', {'form': form})


def func_register(request):
    next = request.GET.get('next')
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'Register.html', {'re_form': form})


def func_logout(request):
    logout(request)
    return redirect('/')


def func_question(request):
    return render(request, 'question.html')


def func_scoreboard(request):
    return render(request, 'scoreboard.html')


@method_decorator(csrf_exempt, name='dispatch')
def func_goBack(request):
    if request.method == "POST":
        return redirect('accounts/login/')
    else:
        return render(request, "LoginError.html")
