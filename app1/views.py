from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import App


def index(request):
    o = App.objects.all()
    return render(request, 'app1/index.html', {'all': o})


def page(request, id):
    p = get_object_or_404(App, pk=id)
    return render(request, 'app1/page.html', {'page': p})