import django_tables2 as tables
from locator.models import Entity


class EntityTable(tables.Table):
	class Meta:
		model = Entity
		# add style="width:80%;" to <table> tag
		attrs = {"style": "width:80%;"}