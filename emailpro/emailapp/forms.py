from . models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        labels = {
            'username':'USERNAME',
            'password':'PASSWORD',
            'email':'E-MAIL'
        }

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Enter Username'}),
            'password':forms.Textarea(attrs={'placeholder':'Enter Password'}),
        }