from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField('название', max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-id']


class Input(models.Model):
    category = models.ForeignKey('Category', related_name='inputs', on_delete=models.CASCADE)
    text = models.CharField('текст', db_index=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']


class Output(models.Model):
    category = models.ForeignKey('Category', related_name='outputs', on_delete=models.CASCADE)
    text = models.TextField('текст')
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']
