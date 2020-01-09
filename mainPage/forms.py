from django import forms

class SettingsForm(forms.Form):
    num1Max = forms.CharField(required = False, 
                                label = "Numbers", 
                                widget=forms.TextInput(attrs={'placeholder': '(1, 10);(1, 10);(1, 10)'}))

    operators = forms.CharField(max_length = 4)
    negativeAnswerAllowed = forms.BooleanField(required = False)
    canExceedTen = forms.BooleanField(required = False)