### Djnago CRUD 24ver

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python.exe -m pip install --upgrade pip
```

```bash
pip install django==3.2.13
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

![image-20240115100941626](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240115100941626.png)

##### 🪐 Articles app 

```bash
python manage.py startapp articles
```

---



#### ◾ CRUD

##### (1) 모델 정의하기 (DB스키마 설계)

```python
from django.db import models

# 게시판의 기능 
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



* ##### migrations 파일 생성

```bash
python manage.py makemigrations
```

* ##### DB 반영

```bash
python manage.py migrate
```

* ##### DB반영 확인

```python
python manage.py showmigrations
```

---



##### 🪐 settings.py

```python
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#...

ROOT_URLCONF = 'articles.urls'

#...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

#...
```



---



##### (2) 기능 구현 



##### 3. articles > urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path("", views.index, name="index"),
    #  create
    path('new/', views.new, name='name'),
    path("create/", views.create, name="create"),
    # content
    path("detail/<int:review_pk>", views.detail, name="detail"),
    #  update
    path("edit/<int:review_pk>", views.edit, name="edit"),
    path("update/<int:review_pk>", views.update, name="update"),
    # delete
    path("delete/<int:review_pk>", views.delete, name="delete"),
    
]
```



##### 3. pjt > urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("".include("articles.urls")),
]
```





##### 4. articles > view.py

```python
from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request, "articles/new.html") 
```



##### 5. Template > new.html

```html
<h1>articles</h1>
<form action=""></form>
```



