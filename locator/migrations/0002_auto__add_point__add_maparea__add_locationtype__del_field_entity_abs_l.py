# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Entity', fields ['name']
        db.delete_unique(u'locator_entity', ['name'])

        # Adding model 'Point'
        db.create_table(u'locator_point', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
        ))
        db.send_create_signal(u'locator', ['Point'])

        # Adding model 'MapArea'
        db.create_table(u'locator_maparea', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locator.Point'])),
            ('height', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('width', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
        ))
        db.send_create_signal(u'locator', ['MapArea'])

        # Adding model 'LocationType'
        db.create_table(u'locator_locationtype', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, primary_key=True)),
        ))
        db.send_create_signal(u'locator', ['LocationType'])

        # Deleting field 'Entity.abs_latitude'
        db.delete_column(u'locator_entity', 'abs_latitude')

        # Deleting field 'Entity.longitude'
        db.delete_column(u'locator_entity', 'longitude')

        # Deleting field 'Entity.abs_longitude'
        db.delete_column(u'locator_entity', 'abs_longitude')

        # Deleting field 'Entity.latitude'
        db.delete_column(u'locator_entity', 'latitude')

        # Adding field 'Entity.location'
        db.add_column(u'locator_entity', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['locator.Point']),
                      keep_default=False)

        # Adding field 'Entity.slug'
        db.add_column(u'locator_entity', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='1', unique=True, max_length=50, primary_key=True),
                      keep_default=False)


        # Renaming column for 'Entity.type' to match new field type.
        db.rename_column(u'locator_entity', 'type', 'type_id')
        # Changing field 'Entity.type'
        db.alter_column(u'locator_entity', 'type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locator.LocationType']))
        # Adding index on 'Entity', fields ['type']
        db.create_index(u'locator_entity', ['type_id'])


        # Changing field 'Entity.name'
        db.alter_column(u'locator_entity', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Removing index on 'Entity', fields ['type']
        db.delete_index(u'locator_entity', ['type_id'])

        # Deleting model 'Point'
        db.delete_table(u'locator_point')

        # Deleting model 'MapArea'
        db.delete_table(u'locator_maparea')

        # Deleting model 'LocationType'
        db.delete_table(u'locator_locationtype')


        # User chose to not deal with backwards NULL issues for 'Entity.abs_latitude'
        raise RuntimeError("Cannot reverse this migration. 'Entity.abs_latitude' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Entity.longitude'
        raise RuntimeError("Cannot reverse this migration. 'Entity.longitude' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Entity.abs_longitude'
        raise RuntimeError("Cannot reverse this migration. 'Entity.abs_longitude' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Entity.latitude'
        raise RuntimeError("Cannot reverse this migration. 'Entity.latitude' and its values cannot be restored.")
        # Deleting field 'Entity.location'
        db.delete_column(u'locator_entity', 'location_id')

        # Deleting field 'Entity.slug'
        db.delete_column(u'locator_entity', 'slug')


        # Renaming column for 'Entity.type' to match new field type.
        db.rename_column(u'locator_entity', 'type_id', 'type')
        # Changing field 'Entity.type'
        db.alter_column(u'locator_entity', 'type', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Entity.name'
        db.alter_column(u'locator_entity', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True))
        # Adding unique constraint on 'Entity', fields ['name']
        db.create_unique(u'locator_entity', ['name'])


    models = {
        u'locator.entity': {
            'Meta': {'object_name': 'Entity'},
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locator.Point']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['locator.LocationType']"})
        },
        u'locator.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'})
        },
        u'locator.maparea': {
            'Meta': {'object_name': 'MapArea'},
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locator.Point']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'width': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'})
        },
        u'locator.point': {
            'Meta': {'object_name': 'Point'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'})
        }
    }

    complete_apps = ['locator']