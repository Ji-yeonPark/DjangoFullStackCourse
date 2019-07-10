# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
# from .models import User
from .forms import NewUserForm

# Create your views here.


def index(request):
    return render(request, 'first_app/index.html')


def users(request):
    # user_list = User.object.order_by('first_name')
    # user_dict = {'users': user_list}
    # return render(request, 'first_app/users.html', context=user_dict)

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('ERROR FROM INVALID')

    return render(request, 'first_app/users.html', {'form': form})
