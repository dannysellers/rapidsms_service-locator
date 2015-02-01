from django.contrib import admin
import models
from leaflet.admin import LeafletGeoAdmin


class EntityAdmin(LeafletGeoAdmin):
	fields = ('name', 'slug', 'type', 'location')
	list_display = ('name', 'slug', 'type')
	list_filter = ['type']
	search_fields = ['name', 'type']


class EntityInline(admin.TabularInline):
	model = models.Entity
	fields = ('name', 'slug', 'type', 'location')


class LocationTypeAdmin(LeafletGeoAdmin):
	def count (self, instance):
		return models.Entity.objects.filter(type = instance).count()

	fields = ('name', 'slug')
	inlines = [EntityInline]
	list_display = ('name', 'count')


class BeaconAdmin(LeafletGeoAdmin):
	fields = ('identifier')


admin.site.register(models.Point, LeafletGeoAdmin)
# admin.site.register(models.Entity, LeafletGeoAdmin)
admin.site.register(models.Entity, EntityAdmin)
admin.site.register(models.LocationType, LocationTypeAdmin)
admin.site.register(models.MapArea, LeafletGeoAdmin)