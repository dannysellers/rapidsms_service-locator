# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EntityAuditLogEntry'
        db.create_table(u'locator_entityauditlogentry', (
            ('created_by', self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'_auditlog_created_locator_entity_set', to=orm['auth.User'])),
            ('created_with_session_key', self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True)),
            ('modified_by', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_auditlog_modified_locator_entity_set', to=orm['auth.User'])),
            ('modified_with_session_key', self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locator.Point'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'_auditlog_locations', to=orm['locator.LocationType'])),
            (u'action_user', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_entity_audit_log_entry', to=orm['auth.User'])),
            (u'action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            (u'action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'locator', ['EntityAuditLogEntry'])

        # Adding model 'LocationTypeAuditLogEntry'
        db.create_table(u'locator_locationtypeauditlogentry', (
            ('created_by', self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'_auditlog_created_locator_locationtype_set', to=orm['auth.User'])),
            ('created_with_session_key', self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True)),
            ('modified_by', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_auditlog_modified_locator_locationtype_set', to=orm['auth.User'])),
            ('modified_with_session_key', self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            (u'action_user', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_locationtype_audit_log_entry', to=orm['auth.User'])),
            (u'action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            (u'action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'locator', ['LocationTypeAuditLogEntry'])

        # Adding model 'MapAreaAuditLogEntry'
        db.create_table(u'locator_mapareaauditlogentry', (
            ('created_by', self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'_auditlog_created_locator_maparea_set', to=orm['auth.User'])),
            ('created_with_session_key', self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True)),
            ('modified_by', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_auditlog_modified_locator_maparea_set', to=orm['auth.User'])),
            ('modified_with_session_key', self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locator.Point'])),
            ('height', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('width', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            (u'action_user', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_maparea_audit_log_entry', to=orm['auth.User'])),
            (u'action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            (u'action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'locator', ['MapAreaAuditLogEntry'])

        # Adding model 'PointAuditLogEntry'
        db.create_table(u'locator_pointauditlogentry', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('created_by', self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'_auditlog_created_locator_point_set', to=orm['auth.User'])),
            ('created_with_session_key', self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True)),
            ('modified_by', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_auditlog_modified_locator_point_set', to=orm['auth.User'])),
            ('modified_with_session_key', self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=10)),
            (u'action_user', self.gf('audit_log.models.fields.LastUserField')(related_name=u'_point_audit_log_entry', to=orm['auth.User'])),
            (u'action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            (u'action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'locator', ['PointAuditLogEntry'])

        # Adding field 'MapArea.created_by'
        db.add_column(u'locator_maparea', 'created_by',
                      self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'created_locator_maparea_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'MapArea.created_with_session_key'
        db.add_column(u'locator_maparea', 'created_with_session_key',
                      self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'MapArea.modified_by'
        db.add_column(u'locator_maparea', 'modified_by',
                      self.gf('audit_log.models.fields.LastUserField')(related_name=u'modified_locator_maparea_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'MapArea.modified_with_session_key'
        db.add_column(u'locator_maparea', 'modified_with_session_key',
                      self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'Entity.created_by'
        db.add_column(u'locator_entity', 'created_by',
                      self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'created_locator_entity_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Entity.created_with_session_key'
        db.add_column(u'locator_entity', 'created_with_session_key',
                      self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'Entity.modified_by'
        db.add_column(u'locator_entity', 'modified_by',
                      self.gf('audit_log.models.fields.LastUserField')(related_name=u'modified_locator_entity_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Entity.modified_with_session_key'
        db.add_column(u'locator_entity', 'modified_with_session_key',
                      self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'LocationType.created_by'
        db.add_column(u'locator_locationtype', 'created_by',
                      self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'created_locator_locationtype_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'LocationType.created_with_session_key'
        db.add_column(u'locator_locationtype', 'created_with_session_key',
                      self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'LocationType.modified_by'
        db.add_column(u'locator_locationtype', 'modified_by',
                      self.gf('audit_log.models.fields.LastUserField')(related_name=u'modified_locator_locationtype_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'LocationType.modified_with_session_key'
        db.add_column(u'locator_locationtype', 'modified_with_session_key',
                      self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'Point.created_by'
        db.add_column(u'locator_point', 'created_by',
                      self.gf('audit_log.models.fields.CreatingUserField')(related_name=u'created_locator_point_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Point.created_with_session_key'
        db.add_column(u'locator_point', 'created_with_session_key',
                      self.gf('audit_log.models.fields.CreatingSessionKeyField')(max_length=40, null=True),
                      keep_default=False)

        # Adding field 'Point.modified_by'
        db.add_column(u'locator_point', 'modified_by',
                      self.gf('audit_log.models.fields.LastUserField')(related_name=u'modified_locator_point_set', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Point.modified_with_session_key'
        db.add_column(u'locator_point', 'modified_with_session_key',
                      self.gf('audit_log.models.fields.LastSessionKeyField')(max_length=40, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'EntityAuditLogEntry'
        db.delete_table(u'locator_entityauditlogentry')

        # Deleting model 'LocationTypeAuditLogEntry'
        db.delete_table(u'locator_locationtypeauditlogentry')

        # Deleting model 'MapAreaAuditLogEntry'
        db.delete_table(u'locator_mapareaauditlogentry')

        # Deleting model 'PointAuditLogEntry'
        db.delete_table(u'locator_pointauditlogentry')

        # Deleting field 'MapArea.created_by'
        db.delete_column(u'locator_maparea', 'created_by_id')

        # Deleting field 'MapArea.created_with_session_key'
        db.delete_column(u'locator_maparea', 'created_with_session_key')

        # Deleting field 'MapArea.modified_by'
        db.delete_column(u'locator_maparea', 'modified_by_id')

        # Deleting field 'MapArea.modified_with_session_key'
        db.delete_column(u'locator_maparea', 'modified_with_session_key')

        # Deleting field 'Entity.created_by'
        db.delete_column(u'locator_entity', 'created_by_id')

        # Deleting field 'Entity.created_with_session_key'
        db.delete_column(u'locator_entity', 'created_with_session_key')

        # Deleting field 'Entity.modified_by'
        db.delete_column(u'locator_entity', 'modified_by_id')

        # Deleting field 'Entity.modified_with_session_key'
        db.delete_column(u'locator_entity', 'modified_with_session_key')

        # Deleting field 'LocationType.created_by'
        db.delete_column(u'locator_locationtype', 'created_by_id')

        # Deleting field 'LocationType.created_with_session_key'
        db.delete_column(u'locator_locationtype', 'created_with_session_key')

        # Deleting field 'LocationType.modified_by'
        db.delete_column(u'locator_locationtype', 'modified_by_id')

        # Deleting field 'LocationType.modified_with_session_key'
        db.delete_column(u'locator_locationtype', 'modified_with_session_key')

        # Deleting field 'Point.created_by'
        db.delete_column(u'locator_point', 'created_by_id')

        # Deleting field 'Point.created_with_session_key'
        db.delete_column(u'locator_point', 'created_with_session_key')

        # Deleting field 'Point.modified_by'
        db.delete_column(u'locator_point', 'modified_by_id')

        # Deleting field 'Point.modified_with_session_key'
        db.delete_column(u'locator_point', 'modified_with_session_key')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'locator.entity': {
            'Meta': {'object_name': 'Entity'},
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'created_locator_entity_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locator.Point']"}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'modified_locator_entity_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['locator.LocationType']"})
        },
        u'locator.entityauditlogentry': {
            'Meta': {'ordering': "(u'-action_date',)", 'object_name': 'EntityAuditLogEntry'},
            u'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_entity_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'_auditlog_created_locator_entity_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locator.Point']"}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_auditlog_modified_locator_entity_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'_auditlog_locations'", 'to': u"orm['locator.LocationType']"})
        },
        u'locator.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'created_locator_locationtype_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'modified_locator_locationtype_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'})
        },
        u'locator.locationtypeauditlogentry': {
            'Meta': {'ordering': "(u'-action_date',)", 'object_name': 'LocationTypeAuditLogEntry'},
            u'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_locationtype_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'_auditlog_created_locator_locationtype_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_auditlog_modified_locator_locationtype_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'locator.maparea': {
            'Meta': {'object_name': 'MapArea'},
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'created_locator_maparea_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locator.Point']"}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'modified_locator_maparea_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'width': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'})
        },
        u'locator.mapareaauditlogentry': {
            'Meta': {'ordering': "(u'-action_date',)", 'object_name': 'MapAreaAuditLogEntry'},
            u'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_maparea_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'_auditlog_created_locator_maparea_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locator.Point']"}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_auditlog_modified_locator_maparea_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'width': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'})
        },
        u'locator.point': {
            'Meta': {'object_name': 'Point'},
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'created_locator_point_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'modified_locator_point_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'})
        },
        u'locator.pointauditlogentry': {
            'Meta': {'ordering': "(u'-action_date',)", 'object_name': 'PointAuditLogEntry'},
            u'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_point_audit_log_entry'", 'to': u"orm['auth.User']"}),
            'created_by': ('audit_log.models.fields.CreatingUserField', [], {'related_name': "u'_auditlog_created_locator_point_set'", 'to': u"orm['auth.User']"}),
            'created_with_session_key': ('audit_log.models.fields.CreatingSessionKeyField', [], {'max_length': '40', 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '10'}),
            'modified_by': ('audit_log.models.fields.LastUserField', [], {'related_name': "u'_auditlog_modified_locator_point_set'", 'to': u"orm['auth.User']"}),
            'modified_with_session_key': ('audit_log.models.fields.LastSessionKeyField', [], {'max_length': '40', 'null': 'True'})
        }
    }

    complete_apps = ['locator']