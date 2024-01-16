### 07_Login,Logout

* ##### Django가 만들어 놓은 이미 존재하는 from

```python
form django.contrib.auth.forms import (
	AuthenticationForm,
    PasswordResetFrom,
    PasswordChangeForm
)
```



* ##### urls.py

```python
import debug_toolbar
from django.conf.urls import include
from shortener.views import index, get_user, register, login_view, logout_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", index, name="index"),
    path("register", register, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("get_user/<int:user_id>", get_user),
]

```

>     path("login", login_view, name="login"),
>     path("logout", logout_view, name="logout"),



* ##### views.py

```python
# 로그인
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)  
        msg = "가입되어 있지 않거나 로그인 정보가 잘못되었습니다"
        print(form.is_valid)  
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None: 
                msg = "로그인 성공"
                login(request, user)
        return render(request, "login.html", {"form": form, "msg": msg})
    else:
        form = AuthenticationForm()  
        return render(request, "login.html", {"form": form})

# 로그아웃
def logout_view(request):
    logout(request)  
    return redirect("index")
```



* ##### login.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Django 24ver</title>
  </head>
  <body>
    <h2>로그인</h2>
    <h4>{% if msg %}{{ msg }}{% endif %}</h4>
    <form method="post">
      {% csrf_token %}{{ form.as_p }}
      <button type="submit">로그인</button>
    </form>
    <a href="{% url 'index' %}">홈으로</a>
    <a href="{% url 'index' %}">회원가입</a>
  </body>
</html>

```

> ![image-20240116131353771](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116131353771.png)



* ##### base.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Django 24ver</title>
  </head>
  <body>
    {{ user }} <br />
    {% for i in params %} {{ i }} <br />
    {% endfor %}{% if user.is_authenticated %}
    <p><a href={% url 'logout' %}>로그아웃</a></p>
    {% else %}
    <a href="{% url 'login' %}">로그인</a>
    <a href="{% url 'register' %}">회원가입</a>
    {% endif  %}
  </body>
</html>

```

![image-20240116132130210](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116132130210.png)
