from django import forms


class UserInputForm(forms.Form):
    text = forms.CharField(required=True, max_length=100)