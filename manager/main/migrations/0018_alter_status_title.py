# Generated by Django 4.2.2 on 2023-09-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_status_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(choices=[('+', 'Завершено'), ('-', 'Не завершено'), ('+/-', 'В процессе')], default='-', max_length=30, verbose_name='Завершенность'),
        ),
    ]
