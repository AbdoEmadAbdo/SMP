 #?     2nd way                  too much    (ونعمل ف ال HTML ,  كل حاجه(فيلدز) فال موودلز بنروح نعملها ف ال فوورمز (وف ال فيووز 
'''
class LoginForm():  
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100 ,default='customer0@gmail.com')
'''

from django import forms
from .models import Login

class LoginForm(forms.Form):
    class Meta:
        model = Login
        fields= '__all__'

