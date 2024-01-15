from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as U
from django.db import models

class PayPlan(models.Model):
    name = models.CharField(max_length = 20)
    price = models.IntegerField()
    update_at = models.DateTimeField(auto_now = True)
    create_at = models.DateTimeField(auto_now_add = True)
class User(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete = models.DO_NOTHING)

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete = models.DO_NOTHING)