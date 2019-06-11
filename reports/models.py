from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from fond.models import *


class ReportModel(models.Model):
    name = models.CharField('Заголовок', max_length=300)
    slug = models.SlugField('url', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заголовок статьи/отчета'
        verbose_name_plural = 'Заголовок статьи/отчета'


class Reportchoice(models.Model):
    name = models.CharField("Название", max_length=500, blank=True, null=True)
    text = RichTextUploadingField('Тело', blank=True, null=True, config_name='default',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor_plugins/youtube/youtube_2.1.13/youtube/',
                                       'plugin.js')])
    rec = models.ForeignKey(ReportModel, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField('url', blank=True, null=True)

    def __str__(self):
        return self.name if self.name else self.slug

    def get_files(self):
        return FilesReports.objects.filter(rec_id=self.id)

    def get_absolute_url(self):
        return reverse('one_report', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'


class FilesReports(models.Model):
    name = models.CharField('Название файла', max_length=300)
    file = models.FileField('Файл', upload_to="files/", max_length=100, null=True, blank=True)
    rec = models.ForeignKey(Reportchoice, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
