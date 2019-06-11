# Generated by Django 2.2.1 on 2019-06-11 17:07

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='url')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fond.CategoryFond')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
        migrations.CreateModel(
            name='Infograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Файл картинки')),
            ],
            options={
                'verbose_name': 'Инфографика',
                'verbose_name_plural': 'Инфографики',
            },
        ),
        migrations.CreateModel(
            name='Vcontrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст')),
                ('slug', models.SlugField(verbose_name='url')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fond.Vcontrol')),
            ],
            options={
                'verbose_name': 'Внутренний контроль',
                'verbose_name_plural': 'Внутренний контроль',
            },
        ),
        migrations.CreateModel(
            name='FilesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Файл')),
                ('control', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fond.Vcontrol')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='CeoFond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото')),
                ('birthday', models.CharField(max_length=100, verbose_name='Дата рождения')),
                ('position', models.CharField(max_length=200, verbose_name='Должность')),
                ('work_period', models.CharField(max_length=200, verbose_name='Период работы')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Подробная биография')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='url')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fond.CategoryFond')),
            ],
            options={
                'verbose_name': 'Руководитель',
                'verbose_name_plural': 'Руководители',
            },
        ),
        migrations.CreateModel(
            name='Aim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Цели и функции')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='url')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fond.CategoryFond')),
            ],
            options={
                'verbose_name': 'Цели и функции',
                'verbose_name_plural': 'Цели и функции',
            },
        ),
    ]
