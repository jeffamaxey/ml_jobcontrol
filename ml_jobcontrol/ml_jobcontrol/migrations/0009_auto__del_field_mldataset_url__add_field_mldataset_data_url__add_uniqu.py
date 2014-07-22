# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MLDataSet.url'
        db.delete_column(u'ml_jobcontrol_mldataset', 'url')

        # Adding field 'MLDataSet.data_url'
        db.add_column(u'ml_jobcontrol_mldataset', 'data_url',
                      self.gf('django.db.models.fields.URLField')(default=u'', unique=True, max_length=200),
                      keep_default=False)

        # Adding unique constraint on 'MLDataSet', fields ['name']
        db.create_unique(u'ml_jobcontrol_mldataset', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'MLDataSet', fields ['name']
        db.delete_unique(u'ml_jobcontrol_mldataset', ['name'])

        # Adding field 'MLDataSet.url'
        db.add_column(u'ml_jobcontrol_mldataset', 'url',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=200, unique=True),
                      keep_default=False)

        # Deleting field 'MLDataSet.data_url'
        db.delete_column(u'ml_jobcontrol_mldataset', 'data_url')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ml_jobcontrol.mlclassificationtestset': {
            'Meta': {'object_name': 'MLClassificationTestSet'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mldataset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLDataSet']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'mlclassificationtestsets'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'test_num': ('django.db.models.fields.IntegerField', [], {}),
            'train_num': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ml_jobcontrol.mldataset': {
            'Meta': {'object_name': 'MLDataSet'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'data_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'mldatasets'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ml_jobcontrol.mljob': {
            'Meta': {'object_name': 'MLJob'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mlclassification_testset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLClassificationTestSet']"}),
            'mlmodel_config': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLModelConfig']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'todo'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"})
        },
        u'ml_jobcontrol.mlmodel': {
            'Meta': {'object_name': 'MLModel'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'mlmodels'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'ml_jobcontrol.mlmodelconfig': {
            'Meta': {'object_name': 'MLModelConfig'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_config': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'mlmodel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mlmodelconfigs'", 'to': u"orm['ml_jobcontrol.MLModel']"})
        },
        u'ml_jobcontrol.mlresultscore': {
            'Meta': {'object_name': 'MLResultScore'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mljob': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scores'", 'to': u"orm['ml_jobcontrol.MLJob']"}),
            'mlscore': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLScore']"}),
            'score': ('django.db.models.fields.FloatField', [], {})
        },
        u'ml_jobcontrol.mlscore': {
            'Meta': {'object_name': 'MLScore'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ml_jobcontrol']