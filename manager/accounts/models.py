from django.db import models
from django.conf import settings
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from main.models import Company


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
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True, verbose_name='Подписчики')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name='Номер телефона')
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, verbose_name="Фото профиля", null=True)
    current_company = models.CharField(default='В поиске работы', max_length=100, verbose_name='Текущая работа')
    country = models.CharField(default='Беларусь', max_length=50, verbose_name='Страна')
    city = models.CharField(blank=True, null=True, verbose_name='Город', max_length=50)
    experience_years = models.IntegerField(verbose_name='Опыт работы (в годах)', default=0, null=True, blank=True)
    experience = models.TextField(verbose_name='Опыт работы', default="Отсутствует", null=True, blank=True)
    education = models.TextField(blank=True, verbose_name='Высшее/средне-специальное образование/курсы', null=True)
    description = models.TextField(blank=True, verbose_name='О себе', null=True)
    contacts = models.TextField(blank=True, verbose_name='Соцсети', null=True)
    skills = models.TextField(verbose_name = 'Профессиональные навыки/интересы', default='Web-разработка')
    job_title = models.CharField(verbose_name = 'Должность', max_length=50, default='Программист')

    def __str__(self):
        return f"Профиль {self.user.username}" 
    
    class Meta:
        verbose_name_plural = "Профили"
        verbose_name = "Профиль"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.photo.path)

    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url



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