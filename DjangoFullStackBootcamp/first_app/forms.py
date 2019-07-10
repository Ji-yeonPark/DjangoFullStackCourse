# -*- coding: utf-8 -*-
from django import forms
from django.core import validators
    
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea)
    
    # clean_필드명
    def clean_botcatcher(self):
            botcatcher = self.cleaned_data['botcatcher']
            if len(botcatcher) > 0:
                raise forms.ValidationError('GOTCHA BOT!')
            return botcatcher

    # 전체 form 제거
    def clean(self):
        all_clean_data = super(FormName, self).clean() 

        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")