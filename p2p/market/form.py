from django import forms
from models import UserModel
# it is the signup form which extends the django forms class
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email','username','name','password']

# it is the log in form which extends the django forms class
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']


