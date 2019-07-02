# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from first_app.models import AccessRecord, Topic, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)