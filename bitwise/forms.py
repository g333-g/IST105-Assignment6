from django import forms
class NumberForm(forms.Form):
    a = forms.IntegerField(min_value=0)
    b = forms.IntegerField(min_value=0)
    c = forms.IntegerField(min_value=0)
    d = forms.IntegerField(min_value=0)
    e = forms.IntegerField(min_value=0)

