from django.shortcuts import render, redirect
from .main import newNumber
from .forms import SettingsForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


# Create your views here.
def math(request):
    settings = [
        [],
        [],
    ]
    context = {}

    if request.method == "POST":
        form = SettingsForm(request.POST)
        if form.is_valid():
            context['form'] = form
            settings[0].append(form.cleaned_data.get('num1Max'))

            add = form.cleaned_data.get('add')
            subtract = form.cleaned_data.get('subtract')
            multiply = form.cleaned_data.get('multiply')
            divide = form.cleaned_data.get('divide')

            if not add and not subtract and not multiply and not divide:
                settings[1].append('+')
            else:
                if add == True:
                    settings[1].append('+')
                if subtract == True:
                    settings[1].append('-')
                if multiply == True:
                    settings[1].append('*')
                if divide == True:
                    settings[1].append('/')
            
            settings.append(form.cleaned_data.get('negativeAnswerAllowed'))
            settings.append(form.cleaned_data.get('canExceedTen'))
            

    elif request.method == "GET":
        context['form'] = SettingsForm()

    returnArr = [];
    newSet = newNumber(*settings)
    for _ in range(100): # Creates the range number of equations.
        returnArr.append(newSet.finalEquation())
    context['numSet'] = returnArr
    return render(request, 'mainPage/math.html', context)

def home(request):
    context = {
        'userList': User.objects.all(),
        }
    return render(request, 'mainPage/home.html', context)

def auth_user(request, username):
    password = 'please3213'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return redirect('mathPage')

def scoreup(request):
    response_data = {}
    
    if request.POST.get('action') == 'POST':
        user = User.objects.get(pk = request.user.pk)
        user.score.score += 10
        user.score.save()
        response_data['currentScore'] = user.score.score
        return JsonResponse(response_data)