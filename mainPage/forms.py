from django import forms

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