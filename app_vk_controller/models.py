from django.db import models

# Create your models here.
from django.urls import reverse


class Account(models.Model):
    # slug = models.SlugField('url', unique=True, max_length=255) #todo

    token = models.CharField(max_length=255)
    first_name = models.CharField('имя', max_length=255)
    last_name = models.CharField('фамилия', max_length=255)
    user_id = models.IntegerField(db_index=True, unique=True)
    photo_url = models.TextField(null=True, blank=True)
    blocked = models.BooleanField('заблокирован', default=False)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    start_status = models.BooleanField('запущен', default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('vk_acc_detail', kwargs={'pk': self.pk})


class User(models.Model):
    # slug = models.SlugField('url', unique=True, max_length=255) #todo
    account = models.ForeignKey('Account', related_name='users', on_delete=models.CASCADE)
    user_id = models.IntegerField(unique=True, db_index=True)
    photo_url = models.TextField(null=True, blank=True)
    state = models.IntegerField('стадия', default=0)
    first_name = models.CharField('имя', max_length=100)
    last_name = models.CharField('фамилия', max_length=100)
    city = models.CharField('город', default='default', max_length=100)
    blocked = models.BooleanField('заблокирован', default=False)
    joined_at = models.DateTimeField('создан', auto_now_add=True)
    updated_at = models.DateTimeField('обновлен', auto_now_add=True)  # todo

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('vk_user_detail', kwargs={'pk': self.pk})


class Numbers(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='numbers')
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='number')
    date = models.DateTimeField('получен', auto_now_add=True)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse('numbers', kwargs={'pk': self.pk})


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


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name='messages', on_delete=models.CASCADE)
    sent_at = models.DateTimeField('получен')
    text = models.TextField('текст')
    answer_question = models.TextField('ответ')
    answer_template = models.TextField('шаблон')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.pk})