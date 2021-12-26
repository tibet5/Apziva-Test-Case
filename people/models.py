from django.db import models
# Create your models here.


class People(models.Model):
    login = models.TextField(
        null=False,
        blank=True
    )
    name = models.TextField(
        max_length=254,
        blank=False,
        null=False
    )
    e_mail = models.EmailField(
        max_length=254
    )
    bio = models.TextField(
        blank=False,
        null=False
    )
    location = models.TextField(
        blank=True,
        null=False
    )
    hireable = models.BooleanField(
        null=True,
        blank=True
    )
    user_url = models.URLField(
        max_length=2000
    )
    avatar_url = models.URLField(
        max_length=2000
    )
    role = models.TextField(
        null=False,
        blank=True
    )

    def __str__(self) -> str:
        return self.name

class Login_list(models.Model):
    login_id = models.TextField(
        blank=False,
        null=False
    )

    def __str__(self) -> str:
        return self.login_id

class Last_url_of_users(models.Model):
    user_url_last = models.URLField(
        max_length=2001
    )

    def __str__(self) -> str:
        return self.user_url_last