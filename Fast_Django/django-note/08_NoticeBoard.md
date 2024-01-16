### 08_NoticeBoard

* ##### Django-seed install 

```bash
pip install django-seed
```

```python
INSTALLED_APPS = [
    #...
    "django_seed",
]
```



```bash
python manage.py seed shortener --number=50
```

* `ModuleNotFoundError: No module named 'psycopg2'` 발생시 명령어 입력 

```bash
pip install psycopg2
```

![image-20240116133707532](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116133707532.png)

![image-20240116133907729](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116133907729.png)



---



* ##### urls.py

```python
path("list", list_view, name="list_view")
```



* ##### views.py

```python
@login_required
def list_view(request):
    page = int(request.GET.get("p", 1))
    users = User.objects.all().order_by("-id")  # 모델 이름을 수정
    paginator = Paginator(users, 1)
    users = paginator.get_page(page)
    return render(request, "borders.html", {"users": users})
```



* ##### board.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Django 24ver</title>
  </head>
  <body>
    <h2>user list</h2>
    <h4>{% if msg %}{{ msg }}{% endif %}</h4>
    <table>
      <thead>
        <th>유저이름</th>
        <th>이메일</th>
        <th>가입일</th>
        <th>페이플랜</th>
      </thead>
      {% for u in users %}
      <tr>
        <td>{{u.username}}</td>
        <td>{{u.email}}</td>
        <td>{{u.date_joined}}</td>
        <td>{{u.pay_plan.name}}</td>
      </tr>
      {% endfor %}
    </table>
    <nav>
      <ul>
        {% if users.has_previous %}
        <li><a href="?p={{ users.previous_page_number }}">이전으로</a></li>
        {% else %}
        <li></li>
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
    </nav>
    <p>
      <a href="{% url 'index' %}">홈으로</a>
      <a href="{% url 'register' %}">회원가입</a>
    </p>
  </body>
</html>

```

![image-20240116140226228](C:\Users\areur\AppData\Roaming\Typora\typora-user-images\image-20240116140226228.png)

> ` {% endfor %} {% if not users|length == 0 %}데이터가 없습니다 {% endif %}`
>
> : user가 없을 경우 
