# Generated by Django 2.2.1 on 2019-06-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportchoice',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Название'),
        ),
    ]
