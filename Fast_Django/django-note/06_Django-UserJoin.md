### 06_Django-회원가입

##### 1. url.py

```python
import debug_toolbar
from django.conf.urls import include
from shortener.views import index, get_user, register
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", index, name="index"),
    path("register", register, name="register"),
    path("get_user/<int:user_id>", get_user),
]
```

> `path("register", register, name="register"),` 추가 하기 
>
> `from shortener.views import index, get_user, register` import 잊지말기 



##### 2. views.py

```python
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_date.get("username")
            raw_password = form.cleaned_date.get("password")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입완료"
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
```

> ##### 1. POST요청 처리 
>
> `if request.method == "POST":`
>
> > HTTP요청이 POST인 경우에만 아래 코드 블록이 실행된다.
>
> ##### 2. RegisterForm 인스턴스 생성 
>
> `form = RegisterForm(request.POST)`
>
> > 사용자 등록 form으로 HTTP POST데이터를 기반으로 인스턴스화된다.
>
> ##### 3. 데이터 유효성 검사 
>
> `if form.is_valid():`
>
> > form 이 유효한지 검사하는 것, 만약 form이 유효하다면 아래의 코드 블록이 실행된다.
>
> ##### 4. 사용자 등록 
>
> `form.save()`
>
> > 유효한 form의 데이터를 사용하여 새로운 사용자를 등록한다. 
>
> ##### 5. 인증 및 로그인 
>
> ```python
> username = form.cleaned_date.get("username")
> raw_password = form.cleaned_date.get("password")
> user = authenticate(username=username, password=raw_password)
> login(request, user)
> ```
>
> > 새로 등록된 user로 로그인 하기 위해 Django의 `authenticate`와 `login` 함수를 사용한다.
>
> ##### 6. msg 설정 
>
> `msg = "회원가입완료"`
>
> > 회원가입 완료시 뜨는 msg
>
> ##### 7. 렌더링 및 응답 
>
> `return render(request, "register.html", {"form": form, "msg": msg})`
>
> > 최종적으로 등록 form과 함께 msg를 포함한 HTML 페이지를 반환하여 user에게 보여준다.
>
> ##### 8. GET 요청처리 
>
> ```python
> else:
>     form = RegisterForm()
>     return render(request, "register.html", {"form": form})
> ```
>
> >  GET 요청인 경우, 빈 폼을 생성하고 이를 user에게 보여주는 HTML 페이지를 반환합니다.



##### 3. template > base.html & register.html

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
    <a href="{% url 'register' %}">회원가입</a>
  </body>
</html>

```

> `<a href="{% url 'register' %}">회원가입</a>`

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Django 24ver</title>
  </head>
  <body>
    <h2>회원가입</h2>
    <h4>{% if msg %}{{ msg }}{% endif %}</h4>
    <form method="post">
      {% csrf_token %}{{ form.as_p }}
      <button type="submit">가입하기</button>
    </form>
    <a href="{% url 'index' %}">홈으로</a>
  </body>
</html>

```



> ![image-20240116113645304](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116113645304.png)
>
> ![image-20240116113706948](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116113706948.png)



##### 4. database확인

