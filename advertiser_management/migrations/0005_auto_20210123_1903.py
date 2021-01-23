# Generated by Django 3.1.5 on 2021-01-23 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertiser_management', '0004_auto_20210123_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('clicks', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=30)),
                ('link', models.URLField(max_length=2000)),
                ('image_url', models.URLField(max_length=2000)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Advertise',
            },
        ),
        migrations.AlterModelManagers(
            name='advertiser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='baseadvertise_ptr',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='username',
        ),
        migrations.AddField(
            model_name='advertiser',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='advertiser',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advertiser',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertiser',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertiser',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Advertise',
        ),
        migrations.DeleteModel(
            name='BaseAdvertise',
        ),
        migrations.AddField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='advertiser_management.advertiser'),
        ),
    ]
