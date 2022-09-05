from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from db.models import User
from db.models import User, SocialPost, TrainingPost


from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.conf import settings

import datetime


ISO_DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

def parseISOFormatOrNone(ISOFormattedString):
    if ISOFormattedString:
        dt_object = datetime.datetime.strptime(
            ISOFormattedString, ISO_DATE_TIME_FORMAT
        )
        return dt_object
    else:
        return None


# registration forms
class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
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
#END class CreateUserForm(UserCreationForm):


class CreateSocialPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(forms.ModelForm, self).__init__(*args, **kwargs)
            self.fields['post_title'].widget.attrs['class'] = 'form-control'
            self.fields['post_title'].widget.attrs['placeholder'] = 'Title'
            self.fields['post_photo'].widget.attrs['class'] = 'form-control  btn'
            self.fields['post_photo'].widget.attrs['placeholder'] = 'qwe1'
            self.fields['post_text'].widget.attrs['class'] = 'form-control'
            self.fields['post_text'].widget.attrs['placeholder'] = 'Post text'

            self.fields['post_is_private'].widget.attrs['placeholder'] = 'Confirm password'

    class Meta:
        model = SocialPost
        fields = (
            'post_title', 
            'post_photo',
            'post_text', 
            'post_is_private')
#END class CreateSocialPostForm(forms.ModelForm):

class CreateTrainingPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(forms.ModelForm, self).__init__(*args, **kwargs)
            self.fields['post_title'].widget.attrs['class'] = 'form-control'
            self.fields['post_title'].widget.attrs['placeholder'] = 'Title'
            self.fields['post_text'].widget.attrs['class'] = 'form-control'
            self.fields['post_text'].widget.attrs['placeholder'] = 'Post text'
            self.fields['datetime_started'].widget.attrs['class'] = 'form-control date-time-picker-needed'
            self.fields['datetime_started'].widget.attrs['placeholder'] = 'Start of activity'
            self.fields['datetime_finished'].widget.attrs['class'] = 'form-control date-time-picker-needed'
            self.fields['datetime_finished'].widget.attrs['placeholder'] = 'End of activity (optional)'
            self.fields['post_is_private'].widget.attrs['placeholder'] = 'Confirm password'
        
    def clean_datetime_started(self):
        return parseISOFormatOrNone(self.data['datetime_started'])

    def clean_datetime_finished(self):
        return parseISOFormatOrNone(self.data['datetime_finished'])

    class Meta:
        model = TrainingPost
        fields = (
            'post_title', 
            'post_text', 
            'datetime_started', 
            'datetime_finished',
            'post_is_private'
        )
#END class CreateTrainingPostForm(forms.ModelForm):
        

# profile_edit_forms


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo', 'username', 'birthday', 'email', 'phone', 'short_bio']
