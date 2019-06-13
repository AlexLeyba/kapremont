from fond.models import *


class ArticleManager(models.Manager):
    """ Методо для реализации поиска по всему сайту"""

    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            try:
                or_lookup = (Q(name__icontains=query) | Q(text__icontains=query))
                qs = qs.filter(or_lookup)
            except:
                or_lookup = Q(name__icontains=query)
                qs = qs.filter(or_lookup)
        return qs


class Bargaining(MPTTModel):
    name = models.CharField('Заголовок', max_length=300)
    text = RichTextUploadingField('Тело', blank=True, null=True, config_name='default',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor_plugins/youtube/youtube_2.1.13/youtube/',
                                       'plugin.js')])
    slug = models.SlugField("url")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    objects = ArticleManager()

    class Meta:
        verbose_name = 'Пункт меню Торги'
        verbose_name_plural = 'Пункты меню Торги'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bar', kwargs={"slug": self.slug})

    def get_files(self):
        return FilesBarModel.objects.filter(bargaining_id=self.id)


class FilesBarModel(models.Model):
    name = models.CharField('Название файла', max_length=300)
    file = models.FileField('Файл', upload_to="files/", max_length=100, null=True, blank=True)
    bargaining = models.ForeignKey(Bargaining, on_delete=models.CASCADE, null=True, blank=True)
    objects = ArticleManager()

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
