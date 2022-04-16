from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True, label="User Name", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(required=False, label="Email", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(
        required = True,
        label = "Password",
        widget = forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required = True,
        label = "Confirm Password",
        widget = forms.PasswordInput(attrs={'placeholder':'Password Confirmation'})
    )


    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class EditProfileForm(forms.ModelForm):
    dob= forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model =UserProfile
        fields="__all__"
        exclude = ('user',)