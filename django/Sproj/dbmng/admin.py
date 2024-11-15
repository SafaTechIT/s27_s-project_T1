from django.contrib import admin
from . import models
# Register your models here.
admin.register(models.users)
admin.register(models.tags)
admin.register(models.post)
admin.register(models.comments)
admin.register(models.reply)

