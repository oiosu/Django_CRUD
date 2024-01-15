### 03. URLs-Views-Models

#### ◾ Part_1

##### 01. URLs.py

```python
from django.contrib import admin
from django.urls import path
from shortener.views import index, redirect_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("redirect", redirect_test),
]
```



##### 02. Views.py

```python
from shortener.models import User
from django.shortcuts import render, redirect

def index(request):
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"
        print(email)
    return render(request, "base.html", {"welcome_msg": f"hello {email}", "hello":"world"})

def redirect_test(request):
    print("go redirect!")

```



##### 03. base.html

> 💡shortener > templates > base.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Django 24ver</title>
  </head>
  <body>
    {{ welcome_msg }}
  </body>
</html>

```

![image-20240115183712101](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240115183712101.png)

---

* base.html 에 `{{ hello }}` 를 추가하게 되면 치환되어 `world`가 출력된다.

> hello Anonymous User! world  

---



##### 04. settings.py

```python
import os
#...
TEMPLATES = [
    {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



#### ◾ Part_2

##### 01. `postman` 설치하기 

#####  

##### 02. urls.py

```python
from django.contrib import admin
from django.urls import path
from shortener.views import index, get_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    # path("redirect", redirect_test),
    path("get_user/<int:user_id>", get_user),
]
```



##### 03. views.py

```python
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

def index(request):
    user = User.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"
    print(email)
    print(request.user.is_authenticated)
    return render(request, "base.html", {"welcome_msg": f"hello {email}", "hello": "world"})

@csrf_exempt
# user_id는 urls.py에서 가져오는 값이다.
def get_user(request, user_id):
    print(user_id)
    if request.method == "GET":
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = User.objects.filter(pk=user_id).first()
        return render(request, "base.html", {"user": user, "params": [abc, xyz]})
    elif request.method == "POST":
        username = request.POST.get("username")
        if username:
            user = User.objects.filter(pk=user_id).update(username=username)
            return JsonResponse({"msg": "you just reached with post method!"})

```

> `@csrf_exempt`



##### 04. base.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Django 24ver</title>
  </head>
  <body>
    {{ user }} <br />
    {% for i in params %} <br />
    {{ i }} <br />
    {% endfor %}
  </body>
</html>

```



