# Generated by Django 4.1.7 on 2023-03-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Кол-во просмотров'),
        ),
    ]
