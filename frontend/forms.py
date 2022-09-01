from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from db.models import User
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.conf import settings


# registration forms
class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            print("hello from __init")
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
            
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs=
                    {'class':'form-control',
                      'aria-label' : 'Username',
                      'aria-describedby' : 'basic-addon1'
            }),
            'email': TextInput(attrs=
                    {'class':'form-control',
                      'aria-label' : 'Username',
                      'aria-describedby' : 'basic-addon1'
            }),
        
        }

        
# profile_edit_forms
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo', 'username', 'birthday', 'email', 'phone', 'short_bio']
