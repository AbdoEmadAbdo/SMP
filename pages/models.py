from django.db import models
from datetime import datetime


class User(models.Model):
      name= models.CharField(max_length=50)
      email=models.EmailField(unique=True ,max_length=100)
      image = models.ImageField(upload_to='photos/%y/%m/%d' ,default='photos/1/1/2001/standardimg.png')
      status= models.BooleanField(default=True)
      createdAcc = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
          return self.name 
     
      class Meta:
         ordering = ['-createdAcc']


class Stocks(models.Model):

     stock_name = models.CharField(unique=True ,max_length=50)
     stock_price = models.DecimalField(max_digits=6,decimal_places=2 ,default=00.00)
     stock_quantity = models.CharField(max_length=50)
     stock_total = models.CharField(max_length=50)
     status= models.BooleanField(default=True)
     
     def __str__(self):
          return self.stock_name

class Customer(models.Model):
     customer_name = models.CharField(max_length=50)
     customer_email = models.EmailField(max_length=100)
     customer_mobile = models.CharField(max_length=50)
     customer_address = models.CharField(max_length=50)
     customer_date = models.DateField(default=datetime.now)
#     customer_time = models.TimeField(null=True)
     
     
     def __str__(self):
          return self.customer_name
     

     #if he Customer
class Login(models.Model):
     usernameL = models.CharField(max_length=50)
     passwordL = models.CharField(max_length=100)
     email=models.EmailField(max_length=100 ,default='customer0@gmail.com')
     
     def __str__(self):
           return self.username
 
   
'''
class OrderItemStockCustomer(models.Model):
     
     orderitemstockcustomer_name = models.CharField(max_length=50)
     orderitemstockcustomer_quantity = models.CharField(max_length=50)
     orderitemstockcustomer_price = models.DecimalField(max_digits=6,decimal_places=2 ,default=00.00)
     orderitemstockcustomer_total = models.CharField(max_length=50)
     orderitemstockcustomer_date = models.DateField(default=datetime.now)
     orderitemstockcustomer_time = models.TimeField(null=True)
     
     def __str__(self):
          return self.orderitemstockcustomer_name

  ''' 

# IN    env\project\pages\templates\pages\index.html:

# {% extends 'base.html' %}

#    {% block content %}

#         .......

#     {% endblock %}



# IN   env\project\pages\templates\base.html:

# <!DOCTYPE html>

# <html lang="en">

# <head>

#     <meta charset="UTF-8">

#     <meta name="viewport" content="width=device-width, initial-scale=1.0">

#     <meta http-equiv="X-UA-Compatible" content="ie=edge">

#     <title>Document</title>

# </head>

# <body>

#     {% block content %}

#     {% endblock content %}

# </body>

# </html> 