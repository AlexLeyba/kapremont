from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.files import File
from django.db.models import Q
from sobstvenikam.models import Sobstvenikam


class ArticleManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(name__icontains=query) | Q(text__icontains=query))
            qs = qs.filter(or_lookup)
        return qs


class CategoryFond(MPTTModel):
    """Пункт меню О фонде"""

    name = models.CharField("Название категории", max_length=100)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField('url', null=True, blank=True)  # при деплое сделать slug обязательным полем

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('o_fonde', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    class MPTTMeta:
        order_insertion_by = ['name']


class Vcontrol(MPTTModel):
    """Внутренний контроль"""
    name = models.CharField('Заголовок', max_length=300)
    text = RichTextUploadingField('Текст', blank=True, null=True, config_name='default',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor_plugins/youtube/youtube_2.1.13/youtube/',
                                       'plugin.js',)])
    slug = models.SlugField("url")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('control', kwargs={"slug": self.slug})

    def get_files(self):
        return FilesModel.objects.filter(control_id=self.id)

    class Meta:
        verbose_name = 'Внутренний контроль'
        verbose_name_plural = 'Внутренний контроль'

    class MPTTMeta:
        order_insertion_by = ['name']


class FilesModel(models.Model):
    name = models.CharField('Название файла', max_length=300)
    file = models.FileField('Файл', upload_to="files/", max_length=100, null=True, blank=True)
    control = models.ForeignKey(Vcontrol, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class CeoFond(models.Model):
    """Руководители фонда"""

    objects = ArticleManager()
    name = models.CharField("ФИО", max_length=100)
    photo = models.ImageField('Фото', upload_to="images/", null=True, blank=True)
    birthday = models.CharField('Дата рождения', max_length=100)
    position = models.CharField('Должность', max_length=200)
    work_period = models.CharField('Период работы', max_length=200)
    text = RichTextUploadingField('Подробная биография', blank=True, null=True, config_name='default',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor_plugins/youtube/youtube_2.1.13/youtube/',
                                       'plugin.js',)])
    category = models.ForeignKey(CategoryFond, on_delete=models.CASCADE)
    slug = models.SlugField('url', null=True, blank=True)  # при деплое сделать slug обязательным полем

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ceo')

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'

    class MPTTMeta:
        order_insertion_by = ['name']


class Aim(models.Model):
    """Цели и функции"""
    objects = ArticleManager()
    name = RichTextUploadingField("Цели и функции", blank=True, null=True, config_name='default',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor_plugins/youtube/youtube_2.1.13/youtube/',
                                       'plugin.js',)])
    category = models.ForeignKey(CategoryFond, on_delete=models.CASCADE)
    slug = models.SlugField('url', null=True, blank=True)  # при деплое сделать slug обязательным полем

    def get_absolute_url(self):
        return reverse('aim', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Цели и функции'
        verbose_name_plural = 'Цели и функции'


class Infograph(models.Model):
    name = models.CharField('Название', max_length=300)
    image = models.ImageField('Картинка', upload_to="images/", null=True, blank=True)
    file = models.FileField('Файл картинки', upload_to="files/", max_length=100, null=True, blank=True)

    def display_text_file(self):
        self.file.open()
        return self.file.file.read().replace('\n', '<br>')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инфографика'
        verbose_name_plural = 'Инфографики'
