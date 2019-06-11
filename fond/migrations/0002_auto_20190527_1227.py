# Generated by Django 2.2.1 on 2019-05-27 12:27

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fond', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryfond',
            options={'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
        migrations.AlterField(
            model_name='aim',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fond.CategoryFond'),
        ),
        migrations.AlterField(
            model_name='ceofond',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fond.CategoryFond'),
        ),
    ]