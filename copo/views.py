from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Questions
from copo.form import QuestionForm


def func_main(request):
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
        return render(request, 'index.html', {'path': request.get_host(), 'all_questions': all_questions})


def func_login(request):
    return render(request, 'login.htm')


def func_question(request):
    return render(request, 'question.html')


def func_scoreboard(request):
    return render(request, 'scoreboard.html')
