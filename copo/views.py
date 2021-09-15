from django.shortcuts import render


def func_main(request):
    return render(request, 'index.html')


def func_login(request):
    return render(request, 'login.htm')


def func_question(request):
    return render(request, 'question.html')


def func_scoreboard(request):
    return render(request, 'scoreboard.html')
