# from _future_ import unicode_literals
from django.shortcuts import render

#create your view here

# signup views


def signup_view(request):
    # business logic.
    if request.method == 'GET':
        # display signup form
        today = datetime.now
        form = SignUpForm()
        template_name = 'signup.html'
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            # insert data to db
            new_user = UserModel(name=name, password=make_password(password), email=email, username=username)
            new_user.save()
            return redirect("/login/")
        else:
            return redirect("/signup/")

    return render(request, template_name, {'form':form},{'today':today})

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
