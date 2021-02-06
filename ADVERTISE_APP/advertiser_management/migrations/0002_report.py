# Generated by Django 3.1.6 on 2021-02-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=100)),
                ('number_of_clicks', models.IntegerField()),
                ('number_of_views', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Report',
            },
        ),
    ]
