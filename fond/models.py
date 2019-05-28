from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class CategoryFond(MPTTModel):
    """Пункт меню О фонде"""
    name = models.CharField("Название категории", max_length=100)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField('url', null=True, blank=True)  # при деплое сделать slug обязательным полем

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('o_fonde')


    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    class MPTTMeta:
        order_insertion_by = ['name']


class CeoFond(MPTTModel):
    """Руководители фонда"""
    name = models.CharField("ФИО", max_length=100)
    photo = models.ImageField('Фото', upload_to="images/", null=True, blank=True)
    birthday = models.CharField('Дата рожения', max_length=100)
    position = models.CharField('Должность', max_length=200)
    work_period = models.CharField('Период работы', max_length=200)
    bio = models.TextField('Подробная биография', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    category = TreeForeignKey(CategoryFond, on_delete=models.CASCADE)
    slug = models.SlugField('url', null=True, blank=True)  # при деплое сделать slug обязательным полем

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('ceo')


class Aim(MPTTModel):
    """Цели и функции"""
    picture = models.ImageField('Картинка', upload_to="images/", null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    info_func = models.TextField(null=True, blank=True)
    other_func = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    category = TreeForeignKey(CategoryFond, on_delete=models.CASCADE)
    slug = models.SlugField('url', null=True, blank=True)  # при деплое сделать slug обязательным полем

    class Meta:
        verbose_name = 'Цели и функции'
        verbose_name_plural = 'Цели и функции'

    class MPTTMeta:
        order_insertion_by = ['info']

    def get_absolute_url(self):
        return reverse('celi')

