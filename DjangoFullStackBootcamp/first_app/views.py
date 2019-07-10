# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms

# Create your views here.


def index(request):
    return render(request, 'first_app/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATIONS SUCCESS!")
            print("name : ", form.cleaned_data['name'])
            print("email : ", form.cleaned_data['email'])
            print("text : ", form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form': form})
