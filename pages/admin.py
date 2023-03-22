from django.contrib import admin
from .models import User , Login , Stocks , Customer

admin.site.register(User)

admin.site.register(Login)

admin.site.register(Stocks)
admin.site.register(Customer)

