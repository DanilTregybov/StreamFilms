# Generated by Django 5.0.2 on 2024-03-12 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_rating_star_options_alter_rating_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor_director',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='actor_director',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='actor_director',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name="Ім'я"),
        ),
        migrations.AddField(
            model_name='actor_director',
            name='name_uk',
            field=models.CharField(max_length=100, null=True, verbose_name="Ім'я"),
        ),
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uk',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='film',
            name='country_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Країна'),
        ),
        migrations.AddField(
            model_name='film',
            name='country_uk',
            field=models.CharField(max_length=30, null=True, verbose_name='Країна'),
        ),
        migrations.AddField(
            model_name='film',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='film',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='film',
            name='tagline_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Гасло'),
        ),
        migrations.AddField(
            model_name='film',
            name='tagline_uk',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Гасло'),
        ),
        migrations.AddField(
            model_name='film',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='film',
            name='title_uk',
            field=models.CharField(max_length=100, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='films_shots',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='films_shots',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='films_shots',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='films_shots',
            name='title_uk',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name="Ім'я"),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_uk',
            field=models.CharField(max_length=100, null=True, verbose_name="Ім'я"),
        ),
    ]
