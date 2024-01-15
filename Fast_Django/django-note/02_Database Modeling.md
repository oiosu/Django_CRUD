### 02. Database Modeling

* DB모델링 이란 

> 어떤 item에 속성 데이터를 사전에 정의하는 것 

* `Django`에서 `id`는 기본값(Primary Key) 정의하지 않아도 자동 정의된다.
* 외래키 (Foreign Key)를 사요하면 뒤에 `xxxx_id`를 자동으로 생성

* `Django` DB 컬럼 타입 
  * CharField (길이가 정해진 문자열)
  *  IntegerField (-2147483648 ~ 2147483647)
  * PositiveIntegerField
  * BigIntegerField (-9223372036854775808 ~ 9223372036854775807)
  * PositiveBigIntegerField
  * DateField (날짜)
  * DatetimeField (날짜 + 시간)
  * BooleanField (True/False)
  * TextField (길이가 정해지지 않은 문자열)
  * EmailField (이메일 포멧)
  * JSONField (Json 포멧)
  * AutoField (Auto Increment 필드 with IntegerField)
  * BigAutoField (Auto Increment 필드 with BigIntegerField)
  * ForeignKey (다른 테이블 PK 참조 필드)

| Users Table | data        |
| ----------- | ----------- |
| pay_plan    | Foreign Key |

| PayPlan    | data          |
| ---------- | ------------- |
| id         | Big Integer   |
| name       | CharField     |
| price      | IntergerField |
| updated_at | DataTimeField |
| created_at | DataTimeField |



##### Model

* shortener > models.py 생성 전에 migrate 하기 

```bash
python manage.py migrate
```

```python
from django.db import models
class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
```

* shortener > models.py 생성 후 migrations 하기 

```bash
python manage.py makemigrations
```

* superuser 생성하기 

```python
python manage.py createsuperuser
```

> ◾username : admin
>
> ◾email : admin@shrinkers.com
>
> ◾password: _ _ _ _
>
> Superuser created successfully.

* DBeaver

> 새 데이터베이스 연결 > db.sqlite3 (path) > 완료 > 테이블 확인

![image-20240115125401981](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240115125401981.png)

> auth_user > data > user 확인

![image-20240115125601488](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240115125601488.png)

> Django에서 확인하기 
>
> ```python
> python manage.py runserver
> ```
>
> `http://127.0.0.1:8000/admin`
>
> ![image-20240115125751917](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240115125751917.png)
>
> 💡 만약 admin의 비밀번호를 잊어버렸다면 다음 명령어를 통해 변경하기 
>
> ```bash
>  python manage.py changepassword admin
> ```
>
> ![image-20240115130218059](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240115130218059.png)





##### UserDatabase

* settings.py

```python
AUTH_USER_MODEL = 'shortener.User'
```

```python
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
    
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pay_plan = models.ForeignKey(PayPlan, on_delete = models.DO_NOTHING)
```

![image-20240115142112819](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240115142112819.png)

> * auth => 인증을 위해 사용하는 데이터 베이스 
> * django => django가 직접 사용하는 데이터 베이스
> * shortener => 만든 app 데이터 베이스

