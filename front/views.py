from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .forms import RegisterForm,LoginForm
from .models import User

def index(request):
    return  render(request,'index.html')

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email=email,password=password).first()
            if user:
                request.session['user_id'] = user.pk
                return redirect(reverse('index'))
            else:
                print ('用户名或者密码错误！')
                return redirect(reverse('login'))

        else:
            print (form.errors)
            return redirect(reverse('login'))

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create(email=email,password=password,username=username,balance=1000)
            return redirect(reverse('login'))
        else:
            print (form.errors)
            return redirect(reverse('register'))

class TransferView(View):
    def get(self,request):
        return render(request,'transfer.html')
    def post(self,request):
        pass