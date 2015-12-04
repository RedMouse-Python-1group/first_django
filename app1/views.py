from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from app1.forms import NewForm
from .models import App


def index(request):
    o = App.objects.all()
    return render(request, 'app1/index.html', {'all': o})


def page(request, id):
    p = get_object_or_404(App, pk=id)
    return render(request, 'app1/page.html', {'page': p})


def comments(request):
    form = NewForm()
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            App.objects.create(**{'field1': request.POST.get('field1'), 'field2': request.POST.get('field2')})
            return HttpResponseRedirect('/')
    return render(request, 'app1/comment.html', locals())