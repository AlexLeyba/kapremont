from fond.models import *
from django.urls import reverse


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


class InfoCoin(models.Model):
    """Информация в желтой плашке на главной"""

    name = models.CharField("Всего собрано", max_length=20)
    all_home = models.CharField('Всего домов', max_length=20)
    paid = models.CharField('Оплачено', max_length=20)
    repaired = models.CharField('Всего отремонтировано', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Всего собрано средств'
        verbose_name_plural = 'Всего собрано средств'


class News(models.Model):
    """Статья"""

    name = models.CharField("Заголовок", max_length=300)
    text = RichTextUploadingField('Тело статьи', blank=True, null=True, config_name='default',
                                  external_plugin_resources=[
                                      ('youtube', '/static/ckeditor_plugins/youtube/youtube_2.1.13/youtube/',
                                       'plugin.js'),
                                      ('justify', '/static/ckeditor_plugins/justify_4.11.4/justify/',
                                       'plugin.js')])
    date = models.DateField("дата", auto_now_add=True)
    picture = models.ImageField("Картинка", upload_to="images/", blank=True)
    objects = ArticleManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single', kwargs={"pk": self.id})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Partners(models.Model):
    """Наши партнеры"""

    picture = models.ImageField('Картинка', upload_to="images/", )
    url = models.CharField('Ссылка', max_length=1000)

    class Meta:
        verbose_name = 'Наши партнеры'
        verbose_name_plural = 'Наши партнеры'
