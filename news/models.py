from django.db import models


class InfoCoin(models.Model):
    """Информация в желтой плашке на главной"""

    all_coin = models.CharField("Всего собрано", max_length=20)
    all_home = models.CharField('Всего домов', max_length=20)
    paid = models.CharField('Оплачено', max_length=20)
    repaired = models.CharField('Всего отремонтировано', max_length=20)

    class Meta:
        verbose_name = 'общая информация'
        verbose_name_plural = 'общая информация'


class News(models.Model):
    """Статья"""

    title = models.CharField("Заголовок", max_length=300)
    text = models.TextField("Тело")
    date = models.DateField("дата", auto_now_add=True)
    picture = models.ImageField("Картинка", upload_to="images/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Partners(models.Model):
    picture = models.ImageField('Картинка', upload_to="images/", )
    url = models.CharField('Ссылка', max_length=1000)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
