from django.shortcuts import render
from .main import newNumber
from django.contrib import messages
from .forms import SettingsForm

# Create your views here.
def home(request):
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
    return render(request, 'mainPage/home.html', context)
