from django import forms
from .models import Settings

# class SettingsForm(forms.ModelForm):
    
#     class Meta:
#         model = Settings
#         fields = ['num1Max', 'num2Max', 'add', 'subtract', 'multiply', 'divide']

# class SettingsForm(forms.Form):
#     num1Max = forms.IntegerField(required = False)
#     num2Max = forms.IntegerField(required = False)
#     add = forms.BooleanField(required = False)
#     subtract = forms.BooleanField(required = False)
#     multiply = forms.BooleanField(required = False)
#     divide = forms.BooleanField(required = False)

class SettingsForm(forms.Form):
    num1Max = forms.CharField(required = False, 
                                label = "Numbers", 
                                widget=forms.TextInput(attrs={'placeholder': '(1, 10);(1, 10);(1, 10)'}))

    add = forms.BooleanField(required = False)
    subtract = forms.BooleanField(required = False)
    multiply = forms.BooleanField(required = False)
    divide = forms.BooleanField(required = False)
    negativeAnswerAllowed = forms.BooleanField(required = False)
    canExceedTen = forms.BooleanField(required = False)