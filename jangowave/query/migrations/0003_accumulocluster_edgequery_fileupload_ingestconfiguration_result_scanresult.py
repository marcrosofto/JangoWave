# Generated by Django 2.2.10 on 2020-02-27 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import query.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('query', '0002_auth_userauths'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccumuloCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance', models.CharField(max_length=255)),
                ('zookeeper', models.CharField(max_length=1024)),
                ('user', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('dataTable', models.CharField(default='shard', max_length=255)),
                ('indexTable', models.CharField(default='shardIndex', max_length=255)),
                ('edgeTable', models.CharField(default='graph', max_length=255)),
                ('reverseIndexTable', models.CharField(default='shardReverseIndex', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EdgeQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=400)),
                ('auths', models.CharField(max_length=400)),
                ('running', models.BooleanField()),
                ('finished', models.BooleanField()),
                ('query_id', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=2550)),
                ('originalfile', models.CharField(default='', max_length=2550)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('status', models.CharField(default='NEW', max_length=20)),
                ('document', models.FileField(blank=True, null=True, upload_to=query.models.update_filename)),
            ],
        ),
        migrations.CreateModel(
            name='IngestConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('post_location', models.CharField(default='', max_length=2550)),
                ('use_provenance', models.BooleanField()),
                ('provenanceTable', models.CharField(default='provenance', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ScanResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_id', models.CharField(max_length=400)),
                ('is_finished', models.BooleanField()),
                ('authstring', models.CharField(max_length=255)),
                ('last_access', models.DateTimeField(auto_now_add=True)),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=2550)),
                ('cf', models.CharField(max_length=2550)),
                ('cq', models.CharField(max_length=2550)),
                ('value', models.CharField(max_length=2550)),
                ('scanResult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.ScanResult')),
            ],
        ),
    ]