from django.contrib import admin
# from django.contrib.gis import admin
import models

# admin.site.register(models.Entity, admin.OSMGeoAdmin)
# admin.site.register(models.MapArea, admin.OSMGeoAdmin)

admin.site.register(models.Point)
admin.site.register(models.Entity)
admin.site.register(models.LocationType)
admin.site.register(models.MapArea)