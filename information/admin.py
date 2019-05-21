from django.contrib import admin
from . import models

admin.site.register([models.Information, models.Type, models.File, models.Image])
