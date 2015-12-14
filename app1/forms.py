from django.utils.translation import ugettext_lazy as _
from django import forms


class NewForm (forms.Form):
    field1 = forms.CharField(label=_('Field1'), max_length=5)
    field2 = forms.CharField(label=_('Field2'), widget=forms.Textarea)
