# Generated by Django 4.1.4 on 2023-01-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_lesson_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='lessons',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='university.lesson'),
        ),
    ]
