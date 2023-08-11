# Generated by Django 4.2.2 on 2023-08-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_status_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(choices=[('-', 'Не завершено'), ('+', 'Завершено'), ('+/-', 'В процессе')], default='-', max_length=30, verbose_name='Завершенность'),
        ),
    ]
