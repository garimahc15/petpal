# Generated by Django 3.1 on 2020-08-16 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20200816_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='catanddog',
            name='desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
