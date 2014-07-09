# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MLDataSet'
        db.create_table(u'ml_jobcontrol_mldataset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
        ))
        db.send_create_signal(u'ml_jobcontrol', ['MLDataSet'])

        # Adding model 'MLClassificationTestSet'
        db.create_table(u'ml_jobcontrol_mlclassificationtestset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('mldataset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ml_jobcontrol.MLDataSet'])),
            ('train_num', self.gf('django.db.models.fields.IntegerField')()),
            ('test_num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ml_jobcontrol', ['MLClassificationTestSet'])

        # Adding model 'MLModel'
        db.create_table(u'ml_jobcontrol_mlmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('import_path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'ml_jobcontrol', ['MLModel'])

        # Adding model 'MLModelConfig'
        db.create_table(u'ml_jobcontrol_mlmodelconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('mlmodel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ml_jobcontrol.MLModel'])),
            ('json_config', self.gf('django.db.models.fields.TextField')(unique=True)),
        ))
        db.send_create_signal(u'ml_jobcontrol', ['MLModelConfig'])

        # Adding model 'MLScore'
        db.create_table(u'ml_jobcontrol_mlscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ml_jobcontrol', ['MLScore'])

        # Adding model 'MLResult'
        db.create_table(u'ml_jobcontrol_mlresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('mlmodel_config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ml_jobcontrol.MLModelConfig'])),
            ('mlclassification_testset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ml_jobcontrol.MLClassificationTestSet'])),
        ))
        db.send_create_signal(u'ml_jobcontrol', ['MLResult'])

        # Adding model 'MLResultScore'
        db.create_table(u'ml_jobcontrol_mlresultscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mlresult', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ml_jobcontrol.MLResult'])),
            ('mlscore', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ml_jobcontrol.MLScore'])),
            ('score', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'ml_jobcontrol', ['MLResultScore'])


    def backwards(self, orm):
        # Deleting model 'MLDataSet'
        db.delete_table(u'ml_jobcontrol_mldataset')

        # Deleting model 'MLClassificationTestSet'
        db.delete_table(u'ml_jobcontrol_mlclassificationtestset')

        # Deleting model 'MLModel'
        db.delete_table(u'ml_jobcontrol_mlmodel')

        # Deleting model 'MLModelConfig'
        db.delete_table(u'ml_jobcontrol_mlmodelconfig')

        # Deleting model 'MLScore'
        db.delete_table(u'ml_jobcontrol_mlscore')

        # Deleting model 'MLResult'
        db.delete_table(u'ml_jobcontrol_mlresult')

        # Deleting model 'MLResultScore'
        db.delete_table(u'ml_jobcontrol_mlresultscore')


    models = {
        u'ml_jobcontrol.mlclassificationtestset': {
            'Meta': {'object_name': 'MLClassificationTestSet'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mldataset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLDataSet']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'test_num': ('django.db.models.fields.IntegerField', [], {}),
            'train_num': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ml_jobcontrol.mldataset': {
            'Meta': {'object_name': 'MLDataSet'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'ml_jobcontrol.mlmodel': {
            'Meta': {'object_name': 'MLModel'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ml_jobcontrol.mlmodelconfig': {
            'Meta': {'object_name': 'MLModelConfig'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_config': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'mlmodel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLModel']"})
        },
        u'ml_jobcontrol.mlresult': {
            'Meta': {'object_name': 'MLResult'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mlclassification_testset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLClassificationTestSet']"}),
            'mlmodel_config': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLModelConfig']"}),
            'scores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ml_jobcontrol.MLScore']", 'through': u"orm['ml_jobcontrol.MLResultScore']", 'symmetrical': 'False'})
        },
        u'ml_jobcontrol.mlresultscore': {
            'Meta': {'object_name': 'MLResultScore'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mlresult': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLResult']"}),
            'mlscore': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ml_jobcontrol.MLScore']"}),
            'score': ('django.db.models.fields.FloatField', [], {})
        },
        u'ml_jobcontrol.mlscore': {
            'Meta': {'object_name': 'MLScore'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ml_jobcontrol']