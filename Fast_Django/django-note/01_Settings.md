### 01. Settings

```bash
python -m venv venv
```

```bash
pip install django
```

```bash
python.exe -m pip install --upgrade pip
```

```bash
pip install django==3.2.13
```

```bash
python manage.py runserver
```

#####  `shortener app ` or `pjt app`

```bash
python manage.py startapp shortener
```

```bash
python manage.py startapp pjt
```

* 가상환경 off

```bash
deactivate
```

* 가상환경 on

```bash
python -m venv venv
```



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



