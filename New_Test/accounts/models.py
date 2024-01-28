from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers_set"
    )
    
    groups = models.ManyToManyField(
        "auth.Group", 
        verbose_name=("groups"),
        blank=True,
        help_text=("The groups this user belongs to."),
        related_name="customuser_groups"  # Change this related_name
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="customuser_permissions"  # Change this related_name
    )
    
    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # 프로필 이미지가 비어있는 경우 기본 이미지 사용
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        default='path/to/default/image.jpg'
    )
    
    def __str__(self):
        return self.user.username

