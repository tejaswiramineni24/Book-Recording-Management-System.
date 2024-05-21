from django import forms

class NewBookForm(forms.Form):
    title     = forms.CharField(label='title:',max_length=100)
    price     = forms.FloatField(label='Price')
    Auther    = forms.CharField(label='Auther')
    Publisher = forms.CharField(label='Publisher')

class searchform(forms.Form):
    title  =   forms.CharField(label='title',max_length=100)    