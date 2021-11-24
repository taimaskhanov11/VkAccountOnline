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


class Account(models.Model):
    token = models.CharField(max_length=255)
    name = models.CharField('имя', max_length=255)
    user_id = models.IntegerField(db_index=True, unique=True)
    blocked = models.BooleanField('заблокирован', default=False)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    start_status = models.BooleanField('запущен', default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Numbers(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField('имя', default='', max_length=100)
    city = models.CharField('город', default='', max_length=100)
    number = models.CharField('номер', default='', max_length=100)
    date = models.DateTimeField('получен', auto_now_add=True)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class User(models.Model):
    account = models.ForeignKey('Account', related_name='users', on_delete=models.CASCADE)
    user_id = models.IntegerField(unique=True, db_index=True)
    state = models.IntegerField('стадия', default=0)
    name = models.CharField('имя', default='default', max_length=100)
    city = models.CharField('город', default='default', max_length=100)
    blocked = models.BooleanField('заблокирован', default=False)
    joined_at = models.DateTimeField('создан', auto_now_add=True)
    updated_at = models.DateTimeField('обновлен', auto_now_add=True)  # todo

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name='messages', on_delete=models.CASCADE)
    sent_at = models.DateTimeField('получен')
    text = models.TextField('текст')
    answer_question = models.TextField('ответ')
    answer_template = models.TextField('шаблон')


    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return self.text
