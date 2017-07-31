# from _future_ import unicode_literals
from django.shortcuts import render

#create your view here

# signup views


def signup_view(request):
    return render(request,'signup.html')

# login view

def login_view(request):
    response_data = {}
    if request.method == 'GET':
        # to do: display login form
        form = LoginForm()
    elif request.method == 'POST':
        # to do: process form data
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # check user exist in db or not
            user = UserModel.objects.filter(username=username).first()
            if user:
                # compare password
                if check_password(password, user.password):
                    # login successful
                    new_token = SessionToken(user=user)
                    new_token.create_token()
                    new_token.save()
                    response = redirect('/feed/')
                    response.set_cookie(key='session_token', value=new_token.session_token)
                    return response
                else:
                    # password incorrect.

                    response_data['message'] = 'Incorrect Password! Please try again!'

    response_data['form'] = form
    return render(request, 'login.html', response_data)


def login_fail(request):
    return render(request,'loginfail.html')

def login_success(request):
    return render(request,'login_success.html')
