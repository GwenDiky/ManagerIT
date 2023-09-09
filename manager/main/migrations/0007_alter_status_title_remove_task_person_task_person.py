# Generated by Django 4.2.2 on 2023-09-05 09:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_alter_status_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(choices=[('-', 'Не завершено'), ('+/-', 'В процессе'), ('+', 'Завершено')], default='-', max_length=30, verbose_name='Завершенность'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='person',
        ),
        migrations.AddField(
            model_name='task',
            name='person',
            field=models.ManyToManyField(blank=True, null=True, related_name='app_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
    ]
