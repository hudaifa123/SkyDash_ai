# Generated by Django 3.1 on 2023-01-22 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=100, null=True)),
                ('profileImage', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=90, scale=0.5, size=[200, 200], upload_to='profileImage')),
                ('monthlyCount', models.CharField(blank=True, max_length=100, null=True)),
                ('subscribed', models.BooleanField(default=False)),
                ('subscriptionType', models.CharField(choices=[('free', 'free'), ('advanced', 'advanced'), ('starter', 'starter')], default='free', max_length=20)),
                ('subscriptionReference', models.CharField(blank=True, max_length=500, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('dateCreated', models.DateTimeField(blank=True, null=True)),
                ('lastUpdated', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
