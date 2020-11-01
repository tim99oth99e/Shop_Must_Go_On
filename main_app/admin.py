from django.contrib import admin

from .models import Shop, City, Category

# Register your models here.
admin.site.register(Shop)
admin.site.register(City)
admin.site.register(Category)