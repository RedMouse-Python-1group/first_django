from django import forms


class NewForm (forms.Form):
    field1 = forms.CharField(max_length=5)
    field2 = forms.CharField(widget=forms.Textarea)
