# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    
    return render(request, 'first_app/index.html', context=date_dict)


def help(request):
    helpdict = {
        'help_insert': 'HELP PAGE!!!'
    }
    return render(request, 'first_app/help.html', context=helpdict)