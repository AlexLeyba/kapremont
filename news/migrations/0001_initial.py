# Generated by Django 2.2.1 on 2019-06-11 17:07

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Всего собрано')),
                ('all_home', models.CharField(max_length=20, verbose_name='Всего домов')),
                ('paid', models.CharField(max_length=20, verbose_name='Оплачено')),
                ('repaired', models.CharField(max_length=20, verbose_name='Всего отремонтировано')),
            ],
            options={
                'verbose_name': 'общая информация',
                'verbose_name_plural': 'общая информация',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Тело статьи')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата')),
                ('picture', models.ImageField(blank=True, upload_to='images/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('url', models.CharField(max_length=1000, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
    ]
