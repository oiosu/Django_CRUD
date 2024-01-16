from django.contrib.auth.models import AbstractUser
from django.db import models

class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='users')

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 삭제: pay_plan 필드
    # pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
