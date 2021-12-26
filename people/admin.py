from django.contrib import admin

from .models import People, Login_list, Last_url_of_users
# Register your models here.

admin.site.register(People)
admin.site.register(Login_list)
admin.site.register(Last_url_of_users)