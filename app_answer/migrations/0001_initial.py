# Generated by Django 4.0 on 2021-12-27 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='app_answer.category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(db_index=True, max_length=255, verbose_name='текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='app_answer.category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]