from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    PROFILE_CHOICES = [
        ('instructor', 'Instrutor'),
        ('player', 'Jogador'),
    ]

    profile = models.CharField(max_length=10, choices=PROFILE_CHOICES)

    def is_instructor(self):
        return self.perfil == 'instructor'

    def is_player(self):
        return self.perfil == 'player'

    def __str__(self):
        return f"{self.username} ({self.get_perfil_display()})"

