# Generated by Django 5.1.6 on 2025-03-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('title', models.CharField(max_length=100, verbose_name='Название произведения')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('days_count', models.PositiveSmallIntegerField(default=1, verbose_name='Количество дней заказа')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('books', models.ManyToManyField(to='main.book')),
            ],
        ),
    ]
