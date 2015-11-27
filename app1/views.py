from django.shortcuts import render

# Create your views here.
from first_django.app1 import App


def index(request):
    var = 1+6
    dr = App.objects.get(field1='bbbb')
    return render(request, 'app1/index.html', {'v': var, 'dr': dr})