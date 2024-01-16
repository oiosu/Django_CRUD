### 09_Bootstrap

* ##### Bootstrap install 

```bash
npm install bootstrap@5.3.2
```

* ##### settings.py

```python
INSTALLED_APPS = [
    #...
    "bootstrap5",
]
```

* ##### base.html

```html
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>  
```

![image-20240116142358413](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116142358413.png)



---



##### ◾Build-in Django Template Tags

> * {% csrf_token  %} 
> * {% cycle "a" "b" %} : for문이 돌아가면서 한번은 a 그리고 b가 출력딤
> * {% extends %} : 반복되는 코드 템플릿 확장해서 사용
> * {% block %}
> * {% if %} {% else %}
> * {% for I in items %}
> * {% includes %}



---



##### ◾base.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Django 24ver</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>  
  </head>
  <body>

        {{ user }} <br />
        {% for i in params %} {{ i }} <br />
        {% endfor %}{% if user.is_authenticated %}
        <p><a href={% url 'logout' %}>로그아웃</a></p>
        {% else %}
        <p><a href="{% url 'login' %}">로그인</a></p>
        <p><a href="{% url 'register' %}">회원가입</a></p>
        {% endif  %}
        
        {% block content %}
        {% endblock %}
  </body>
</html>

```

>         {% block content %}
>         {% endblock %}



* ##### borders.html

```html

{% extends "base.html" %}
{% block content %}

    <h2>user list</h2>

    <h4>{% if msg %}{{ msg }}{% endif %}</h4>
    <table class="table table-bordered">
      <thead>
        <th>유저이름</th>
        <th>이메일</th>
        <th>가입일</th>
        <th>페이플랜</th>
      </thead>
      {% for u in users %}
      <tr class={% cycle "tabel-dark" ""%}>
        <td>{{u.username}}</td>
        <td>{{u.email}}</td>
        <td>{{u.date_joined}}</td>
        <td>{{u.pay_plan.name}}</td>
      </tr>
      {% endfor %}
    </table>

      <ul>
        {% if users.has_previous %}
        <li><a href="?p={{ users.previous_page_number }}">이전으로</a></li>
        {% else %}
        <li><a href="#">이전으로</a></li>
        {% endif %}
        <li>
          <a href="#"> {{ users.number }}/{{ users.paginator.num_pages }} </a>
        </li>
        {% if users.has_next %}
        <li><a href="?p={{ users.next_page_number }}">다음으로</a></li>
        {% else %}
        <li><a href="#">다음으로</a></li>
        {% endif %}
      </ul>

    <p>
      <a href="{% url 'index' %}">홈으로</a>
      <a href="{% url 'register' %}">회원가입</a>
    </p>

{% endblock %}


```

> ```html
> {% extends "base.html" %}
> {% block content %}
> 
> ...
> 
> {% endblock %}
> ```



---



##### ◾include_test.html 생성

```html
<p>include ing</p>
```

##### ◾borders.html 생성

```html
{% include "include_test.html" %}
```

##### ◾ 결과

![image-20240116161440902](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116161440902.png)



---



◾ `    <td>{{u.email|email_ma}}</td>`

![image-20240116164148554](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116164148554.png)
