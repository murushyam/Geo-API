from django.contrib import admin

from .models import Incidences,Counties
from leaflet.admin import LeafletGeoAdmin
from leaflet.admin import LeafletWidget
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    list_display=('name','location')

class CountiesAdmin(LeafletGeoAdmin):
    list_display=('adm1name','pop2020')


admin.site.register(Incidences,IncidencesAdmin)
admin.site.register(Counties,CountiesAdmin)

