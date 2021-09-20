import filecmp
import os
import subprocess
from subprocess import call

from django.core.files.storage import FileSystemStorage

from MIL.settings import BASE_DIR
from django.core.files.base import ContentFile
from django.http import HttpResponse
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

from .models import Questions, Score
from copo.form import *


def func_main(request):
    if request.user.is_authenticated:
        print(request.user.username)
        if request.method == "POST":
            new_question = Questions(title=request.POST['title'], description=request.POST['description'],
                                     in_txt=request.FILES['in'], out_txt=request.FILES['out'])
            new_question.save()
            with open(
                    str(BASE_DIR) + '/media/' + str(
                        Questions.objects.get(title=request.POST['title']).id) + '/ex_out.txt',
                    'a') as c:
                c.close()
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


def func_question(request, qid=-1):
    if request.user.is_authenticated:
        if request.method == "POST":
            if qid != -1:
                with open('media/' + str(qid) + '/in.txt', 'rb', 0) as a, open('media/' + str(qid) + '/out.txt',
                                                                               'w+') as b, open(
                    'media/' + str(qid) + '/ex_out.txt', 'a') as c:
                    handle_uploaded_file(request.FILES['answer'], 'media/' + str(qid))
                    our_dir = os.path.abspath("views.py")
                    full_path = str(our_dir).replace("views.py", "media/" + str(qid))
                    subprocess.call(['python3', 'wrapper.py'], stdin=a, stdout=b,
                                    cwd=full_path)
                    result = filecmp.cmp(full_path + "/ex_out.txt", full_path + "/out.txt")
                    if result:
                        score = Score.objects.filter(user=request.user)
                        if not score.exists():
                            s = Score(user=request.user, score=100)
                            s.save()
                        else:
                            score = Score.objects.get(user=request.user)
                            a = score.score+100
                            Score.objects.filter(id=score.id).update(score=a)
                        return HttpResponse('Wone!')
                    else:
                        return HttpResponse('Lose')
        if qid == -1:
            return HttpResponse('Please select a question first')
        else:
            question = Questions.objects.filter(id=qid)
            if not question.exists():
                return HttpResponse('no question found!')
            return render(request, 'question.html', {'question': Questions.objects.get(id=qid)})
    else:
        return redirect('accounts/login/')


def handle_uploaded_file(f, path):
    with open(path + '/wrapper.py', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def func_scoreboard(request):
    list_users = Score.objects.order_by('-score')
    return render(request, 'scoreboard.html', {'user_list': list_users})


@method_decorator(csrf_exempt, name='dispatch')
def func_goBack(request):
    if request.method == "POST":
        return redirect('accounts/login/')
    else:
        return render(request, "LoginError.html")
