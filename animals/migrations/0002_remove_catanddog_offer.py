# Generated by Django 3.1 on 2020-08-13 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catanddog',
            name='offer',
        ),
    ]
