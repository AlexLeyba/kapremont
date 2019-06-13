from mptt.models import MPTTModel
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


class Sobstvenikam(MPTTModel):
    objects = ArticleManager()
    name = models.CharField('Заголовок', max_length=300)
    text = RichTextUploadingField('Тело', blank=True, null=True, config_name='default',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor_plugins/youtube/youtube_2.1.13/youtube/',
                                       'plugin.js')])
    slug = models.SlugField("url")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Пункт меню Собственникам'
        verbose_name_plural = 'Пункты меню Собственникам'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sob', kwargs={"slug": self.slug})

    def get_files(self):
        return FilesSobModel.objects.filter(sobstvenikam_id=self.id)


class RecommendationsSob(models.Model):
    objects = ArticleManager()
    name = models.CharField('Заголовок', max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рекомендации Собственникам'
        verbose_name_plural = 'Рекомендации Собственникам'


class Choices(models.Model):
    choices = models.CharField("Название", max_length=500, default='')
    rec = models.ForeignKey(RecommendationsSob, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField('url', blank=True, null=True)

    def __str__(self):
        return self.choices

    def get_files(self):
        return FilesSobModel.objects.filter(rec_id=self.id)

    def get_absolute_url(self):
        return reverse('one_rec', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Вкладка в рекомендациях'
        verbose_name_plural = 'Вкладки в рекомендациях'


class FilesSobModel(models.Model):
    objects = ArticleManager()
    name = models.CharField('Название файла', max_length=300)
    file = models.FileField('Файл', upload_to="files/", max_length=100, null=True, blank=True)
    sobstvenikam = models.ForeignKey(Sobstvenikam, on_delete=models.CASCADE, null=True, blank=True)
    rec = models.ForeignKey(Choices, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
