# views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    logout(request)
    return HttpResponseRedirect(reverse('form_page', args=request))


def form_name_view(request):
    form = forms.UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('success'))
        else:
            pass
    return render(request, 'form_page.html', {'form': form})


@login_required
def success(request):
    return render(request, 'success_page.html')
