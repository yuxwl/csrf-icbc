#!/usr/bin/env python
# _*_coding:utf-8_*_
''' 
    * @author: Xwl_Yu.
'''
from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=20)
    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError('两次密码输入不一致！')
        return cleaned_data
    class Meta:
        model=User
        fields = ['username','password','email']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

class TransferForm(forms.Form):
    email = forms.CharField(max_length=100)
    money = forms.FloatField()
