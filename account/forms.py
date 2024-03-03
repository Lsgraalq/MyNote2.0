from django import forms
from django.contrib.auth.models import User 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta: 
        model = User 
        fields = ['username', 'first_name','email']
    
    def clean_password2(self):
        cd = self.cleaned_data 
        if cd ['password'] != cd['password2']:
            raise forms.ValidationError('Password don`t match')
        return cd['password2']
    
    # def __init__(self,*args, **kwargs):
    #     super(UserRegistrationForm, self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['password'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'