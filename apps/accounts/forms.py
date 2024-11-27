from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username"}
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}
        )
    )
    
class RegisterForm(UserCreationForm):    
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "date_of_birth",
            "phone_number"
        )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username"}
        )
    )
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First Name"}
        )
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name"}
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Email Address"}
        )
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}
        )
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password"}
        )
    )
    
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2025))
    )
    
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        label="Phone Number",
        widget=forms.TextInput(
            attrs={"placeholder": "Phone Number"}
        )
    )
    

        
        