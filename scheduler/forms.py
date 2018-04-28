from django import forms

class TestForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    age = forms.IntegerField(label="Your Age")
    about_me = forms.CharField(label="About Me", max_length=300)
