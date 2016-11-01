from django.contrib import admin

from . import models


class Topic(admin.ModelAdmin):
    pass


admin.site.register(models.Topic, Topic)

