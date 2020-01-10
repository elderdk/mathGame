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
    
            # add the numbers
            num1Max = form.cleaned_data.get('num1Max')

            if num1Max == '':
                settings[0].append(request.user.defaultsetting.eqArr)
            else:
                settings[0].append(form.cleaned_data.get('num1Max'))
            
            # add the operators
            operators = form.cleaned_data.get('operators')

            if operators == '':
                settings[1].append(request.user.defaultsetting.allowedOperators)
            else:
                settings[1].append(operators)
                
            # add other variables
            settings.append(form.cleaned_data.get('negativeAnswerAllowed'))
            
    elif request.method == "GET":

        # add the numbers
        settings[0].append(request.user.defaultsetting.eqArr)

        # add the operators
        settings[1].append(request.user.defaultsetting.allowedOperators)

        # add other variables
        settings.append(request.user.defaultsetting.negativeAnswerAllowed)

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

        if request.POST['is_correct'] == 'correct':
            if request.POST['is_bonus'] == 'true':
                user.score.score += 20
            else:
                user.score.score += 10
        else:
            if request.POST['is_skull'] == 'true':
                user.score.score -= 20
            pass

        user.score.save()
        response_data['currentScore'] = user.score.score
        return JsonResponse(response_data)