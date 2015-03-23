from django.contrib import admin
from locations.models import *
# Register your models here.




admin.site.register(Datacenters)
admin.site.register(Cages)
admin.site.register(CageRows)
admin.site.register(Racks)