
from django.shortcuts import render
from .forms import TaskForm

def index(request):

    initial_password = 'admin'
    initial_login = 'admin'
    form = TaskForm(initial={'password' : initial_password, 'login' : initial_login})
    success_message = ""

    if request.method == "GET":
        print('new')
        form = TaskForm(request.GET)
        if form.is_valid():
            print("captcha - valid")
            
            user_login = form.cleaned_data['login']
            user_password = form.cleaned_data['password']
            
            if user_password == initial_password and user_login == initial_login:
                print('pass and login - valid')
                form = TaskForm()
                success_message = "Login successful"
            else:
                print('pass or login - invalid')
                success_message = "Invalid login or password"

        else:
            print("captcha - invalid")
    else:
        form = TaskForm()
        
    context = {"form": form, "success_message": success_message}
    return render(request, 'index.html', context)
