from django.db import models


class Product(models.Model):
    number_product = models.PositiveIntegerField(verbose_name='Код')
    title = models.CharField(verbose_name='Наименование', max_length=100, db_index=True)
    price = models.DecimalField(verbose_name='Цена в евро по курсу НБРБ на дату расчета', max_digits=6, decimal_places=2)
    stock = models.DecimalField(verbose_name='Остаток на конец', max_digits=6, decimal_places=2)
    massa = models.DecimalField(verbose_name='Средний вес мешка', max_digits=6, decimal_places=2)
    stock_in_bag = models.PositiveIntegerField(verbose_name='Количество вещей в мешке')
    avg_price = models.DecimalField(verbose_name='Средняя себестоимость вещи руб.', decimal_places=2, max_digits=6)
    published_at = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Customer(models.Model):
    phone = models.CharField(verbose_name='Номер телефона', max_length=25)
    complete = models.BooleanField(verbose_name='Обработано', default=False)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Contact(models.Model):
    phone = models.CharField(verbose_name='Номер телефона', max_length=25)
    city = models.CharField(verbose_name='Город', max_length=100)
    street = models.CharField(verbose_name='Улица', max_length=100)
    number = models.CharField(verbose_name='Номер дома', max_length=5)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class URL(models.Model):
    short_name = models.CharField(verbose_name='Описание видео', max_length=100)
    url = models.URLField(verbose_name='Ссылка для видео')

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
