from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'photo']
        
    
class UserRegistrationForm(UserCreationForm):
    email: forms.EmailField() # type: ignore
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email