from django.db import models
from datetime import datetime

# Create your models here.
class Clothes(models.Model):
    title=models.CharField('Название',max_length=50)
    anons=models.CharField('Описание',max_length=250)
    full_text=models.TextField('Текст')
    tags=models.TextField('Теги темы',default='')
    author=models.CharField('Автор',max_length=100)
    types=models.CharField('Типы',max_length=100)
    pricing=models.CharField('Цена',max_length=100)
    date=models.DateTimeField('Дата создания',default=datetime.now)
    isopub=models.BooleanField('Выложено',default=True)

    def __str__(self):
        return self.title