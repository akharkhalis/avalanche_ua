from django.contrib import admin
from .models.activity_db import activity_db
from .models.locations import locations
from .models.direction import direction
from .models.triger import triger
from .models.aval_type import aval_type


# Register your models here.

admin.site.register(activity_db)
admin.site.register(locations)
admin.site.register(direction)
admin.site.register(triger)
admin.site.register(aval_type)
