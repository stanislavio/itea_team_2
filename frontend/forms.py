from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from db.models import User
from db.models import User, SocialPost, TrainingPost


from django import forms
from django.forms.widgets import TextInput, PasswordInput

import datetime


#registration forms
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


class CreateSocialPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(forms.ModelForm, self).__init__(*args, **kwargs)
            self.fields['post_title'].widget.attrs['class'] = 'form-control'
            self.fields['post_title'].widget.attrs['placeholder'] = 'Title'
            
        #     self.fields['post_photo'].widget.attrs['class'] = 'form-control  btn'
        #     self.fields['post_photo'].widget.attrs['placeholder'] = 'qwe1'
            
            self.fields['post_text'].widget.attrs['class'] = 'form-control'
            self.fields['post_text'].widget.attrs['placeholder'] = 'Post text'

            self.fields['post_is_private'].widget.attrs['placeholder'] = 'Confirm password'

    # def clean(self):
    #     print("I am clean method of CreateSocialPostForm.")
    #     print(self.data)

    

    class Meta:
        model = SocialPost
        fields = ('post_title', 'post_text', 'post_is_private')

class CreateTrainingPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(forms.ModelForm, self).__init__(*args, **kwargs)
            self.fields['post_title'].widget.attrs['class'] = 'form-control'
            self.fields['post_title'].widget.attrs['placeholder'] = 'Title'
            self.fields['post_text'].widget.attrs['class'] = 'form-control'
            self.fields['post_text'].widget.attrs['placeholder'] = 'Post text'
            self.fields['post_is_private'].widget.attrs['placeholder'] = 'Confirm password'
        
    def clean_datetime_started(self):
        print("modelForm clean", self.data['datetime_started'])
        format = "%Y-%m-%dT%H:%M:%S.%fZ"
        dt_object = datetime.datetime.strptime(
            self.data['datetime_started'], format
        )
        return dt_object


    class Meta:
        model = TrainingPost
        fields = ('post_title', 'post_text', 'datetime_started', 'post_is_private')
#END class CreateTrainingPostForm(forms.ModelForm):
        

#profile_edit_forms
class ProfileEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['photo', 'username', 'email', 'birthday', 'phone', 'short_bio' ]

        


