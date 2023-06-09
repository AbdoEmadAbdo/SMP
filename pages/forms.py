 #?     2nd way                  too much    (ونعمل ف ال HTML ,  كل حاجه(فيلدز) فال موودلز بنروح نعملها ف ال فوورمز (وف ال فيووز 
'''
class LoginForm():  
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100 ,default='customer0@gmail.com')
'''
#!To create a form Directly for this model

from django import forms
from .models import Login

class LoginForm(forms.Form):
    class Meta:
        model = Login
        fields= '__all__'
        
   # roll_number = forms.IntegerField(
   #                  help_text = "Enter 6 digit roll number"
   #                  )
   # password = forms.CharField(widget = forms.PasswordInput())



class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search'}))
    



from crispy_forms.helper import FormHelper  #defining a custom layout using the (FormHelper class) ,, and the (Layout, Submit, Row, and Column classes) from Django Crispy Forms.
from crispy_forms.layout import Layout, Submit, Row, Column





class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'message',
            Submit('submit', 'Send Message')
        )
        self.helper.form_method = 'POST'
        self.helper.form_action = 'contact'
  
  
  
  
  
  # in the HTML
  #    {% csrf_token %}
  #    {% crispy form %}  

