# Generated by Django 4.2.2 on 2023-09-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_status_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(choices=[('-', 'Не завершено'), ('+/-', 'В процессе'), ('+', 'Завершено')], default='-', max_length=30, verbose_name='Завершенность'),
        ),
    ]
