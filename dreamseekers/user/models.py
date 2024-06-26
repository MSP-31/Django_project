from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    
    def __str__(self): 
        return self.username
    
    class Meta:
        verbose_name = '유저'
        verbose_name_plural = '유저'