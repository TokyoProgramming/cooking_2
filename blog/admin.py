from django.contrib import admin

from . import models

admin.site.register(models.featuredPost)
admin.site.register(models.Post)
