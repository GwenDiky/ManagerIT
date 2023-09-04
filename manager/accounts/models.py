from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name="Пользователь")
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, verbose_name="Фото профиля")

    def __str__(self):
        return f"Профиль {self.user.username}" 
    
    class Meta:
        verbose_name_plural = "Профили"
        verbose_name = "Профиль"


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} подписан на {self.user_to}'