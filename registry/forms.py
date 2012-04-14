from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from registry.models import UserProfile

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=widgets.PasswordInput(render_value = True))
    confirm_password = forms.CharField(widget=widgets.PasswordInput(render_value = True))
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    
    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        if not cleaned_data.get("password") == cleaned_data.get("confirm_password"):
            raise forms.ValidationError("The entered passwords do not match.")
        return cleaned_data
     
    def clean_username(self):
        data = self.cleaned_data['username']
        try:
            User.objects.get(username=data)
            raise forms.ValidationError("That username is already taken.")
        except User.DoesNotExist: 
            return data
    
    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            User.objects.get(email=data)
            raise forms.ValidationError("That email id is already being used.")
        except User.DoesNotExist: 
            return data
        
class UserProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user')
