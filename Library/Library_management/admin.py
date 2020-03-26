from django.contrib import admin
from .models import *
# Register your models here.
for i in [User,Subscribe,BookCategory,Book,Record,BlackList]:
    admin.site.register(i)


