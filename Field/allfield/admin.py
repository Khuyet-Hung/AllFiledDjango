from django.contrib import admin
from . import models
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Field, AuthorAdmin)