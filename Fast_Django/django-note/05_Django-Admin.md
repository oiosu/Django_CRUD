### 05. Django Admin

* ##### admin.py

```python
from django.contrib import admin
from shortener.models import PayPlan
# Register your models here.
admin.site.register(PayPlan)
```



* ##### admin 로그인 다시 설정 & 비밀번호 잊었을 경우 

```bash
$ python manage.py createsuperuser
```

```bash
$ python manage.py changepassword admin
```



![image-20240116104015193](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116104015193.png)



---

##### ⭐ 오류 해결 ⭐

(1) `TypeError: OneToOneField.__init__() missing 1 required positional argument: 'on_delete'`

>  `pay_plan = models.ForeignKey(PayPlan, on_delete = models.DO_NOTHING)`의 `on_delete` 오타 확인하기 

> 참고자료 : `https://gomguard.tistory.com/101`



(2) No changes detected

> `python manage.py makemigrations` 실행시 발생하는 오류 

```bash
$ python manage.py makemigrations app_name
```

> 뒤에 `app_name` 붙여주면 해결됨 



(3) `django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency shortener.0001_initial on database 'default'.`

> `__init__` 파일 을 제외한 migrations 파일 모두 삭제한다
>
> `db.sqlite3` 파일을 삭제한다. 
>
> 다시 `migrations`을 진행 한다. 

> 참고자료 : `https://blue-coding-story.tistory.com/177`



(4) `django.db.utils.IntegrityError: NOT NULL constraint failed: shortener_user.pay_plan_id` 

> `python manage.py createsuperuser` 설정 다 하면 생기는 오류 
>
> models.py 코드 다음과 같이 수정 후 오류 해결 
>
> ```python
> from django.contrib.auth.models import AbstractUser
> from django.db import models
> 
> class PayPlan(models.Model):
>     name = models.CharField(max_length=20)
>     price = models.IntegerField()
>     update_at = models.DateTimeField(auto_now=True)
>     create_at = models.DateTimeField(auto_now_add=True)
> 
> class User(AbstractUser):
>     pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='users')
> 
> class UserDetail(models.Model):
>     user = models.OneToOneField(User, on_delete=models.CASCADE)
>     # 삭제: pay_plan 필드
>     # pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
> 
> ```
>
> 다시 makemigrations, migrate 명령어 실행 후 `python manage.py createsuperuser` 설정 완료
>
> `Superuser created successfully.`



