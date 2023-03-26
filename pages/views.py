from pymongo import MongoClient
from django.shortcuts import render
from django.template import loader

from .forms import LoginForm
from .models import Login ,Stocks, Customer
#from django.contrib.auth.decorators import login_required


#@login_required(login_url="/login/")
def index(request): 
    # the 3rd way   
    if request.method == 'POST':
       dataform= LoginForm(request.POST)
       if dataform.is_valid():
        dataform.save()
  
    
        # x                         from html  للطريقة الاولي فورم    
    # userName = request.POST.get('User-name')  # el  x  deh   shayla the value of username
    # passWord = request.POST.get('U_password')
    # email = request.POST.get('email')
    # Login(usernameL='userName', passwordL='passWord').save()
    
    ##? But for 2nd way ----> get(....)  will be from the {{{forms.py }}}
    #?  userName = request.POST.get('username')  # from forms.py  username, password
    #? userName = request.POST.get('password')
    #? email = request.POST.get('email')
        
   #?  dataform= Login(usernameL='userName', passwordL='passWord').save()    #data = Login.objects.all()
    #  dataform.save()

    return render(request, 'pages/index.html' , { 'lf': LoginForm } )


def search(request):
    query = request.GET.get('s')
    client = MongoClient()
    db = client['FTKP_DB']
    results = db.my_collection.find({'$text': {'$search': query}})
    return render(request, 'search_results.html', {'results': results})


def sign_in(request):
    return render(request , 'pages/sign_in.html')

def sign_up(request):
    return render(request , 'pages/sign_up.html')

def profile(request):
    return render(request , 'pages/profile.html')

def setting(request):
    return render(request, "pages/setting.html")


def Companys(request):
    
    
    return render(request, "pages/Companies.html")



def LastNews(request):
    return render(request, "pages/LastNews.html")

def Trending(request):
    return render(request, "pages/Trending.html")

def chart(request):
    return render(request, "pages/Chart.html")

def Community(request):
    return render(request, "pages/Community.html")



#to render Jinja2 templates.    When the view is called, it will pass the my_data dictionary to the template, which will use the Jinja2 syntax to insert the name and age variables into the HTML output. 
#                               The final result will be a rendered HTML page that displays the name and age of the user.
def my_view(request):
    my_data = {'name': 'EAA', 'age': 30}
    return render(request, 'pages/my_template.html', my_data)