from django.db import models
from django.conf import settings
from PIL import Image

class Profile(models.Model):
    MALE = 'М'
    FEMALE = "Ж"
    NONE = "-"
    GENDERS = {
        (MALE, "Мужской"),
        (FEMALE, "Женский"),
        (NONE, "Неопределен")
    }

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name="Пользователь")
    sex = models.CharField(max_length=30, verbose_name='Гендер', choices=GENDERS, blank=True, null=True)
    phone_number = models.CharField(("Мобильный телефон номер"), null=True, blank=True, max_length=10)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, verbose_name="Фото профиля")

    def __str__(self):
        return f"Профиль {self.user.username}" 
    
    class Meta:
        verbose_name_plural = "Профили"
        verbose_name = "Профиль"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.photo.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.photo.path)



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