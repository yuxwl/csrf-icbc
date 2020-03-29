#!/usr/bin/env python
from .models import User
from django.shortcuts import redirect,reverse

def login_required(func):
    def wrapper(request,*args,**kwargs):
        if request.front_user:
            return func(request,*args,**kwargs)
        else:
            return redirect(reverse('login'))

    return wrapper