# Generated by Django 3.1.3 on 2020-11-21 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Contact',
            field=models.IntegerField(),
        ),
    ]
