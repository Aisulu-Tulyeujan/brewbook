from django.contrib import admin
from .models import User, Drink, Liked
# Register your models here.

admin.site.register(User)
admin.site.register(Drink)
admin.site.register(Liked)
