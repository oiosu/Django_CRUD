# Django CRUD 

![image-20221004141546130](../imges/Django CRUD/image-20221004141546130.png)

![image-20221004141641616](../imges/Django CRUD/image-20221004141641616.png)



---



### <span style='background-color:#fff5b1'>ย  ย ๐ฃ CRUDย  ย </span>



##### 1) ๊ฐ์ํ๊ฒฝ ์ค์นํ๊ธฐ 

> ##### ๊ฐ์ํ๊ฒฝ ์ค์น๋ฅผ ์ ํ๋ ๊ฑธ๊น?  => ํจํค์ง๋ฅผ ๋ณ๋๋ก ๊ฐ์ ธ๊ฐ๊ธฐ ์ํด ์ค์นํ๋ค. 

```bash
$ python -m venv venv
```

![image-20221004144830298](../imges/Django CRUD/image-20221004144830298.png)

* ##### ativate  ์คํ์ด ํต์ฌ 

```bash
$ source venv/Scripts/activate 
(venv)
```



##### 2) Django ์ค์น 

```bash
$ pip install django==3.2.13
```

![image-20221004145343621](../imges/Django CRUD/image-20221004145343621.png)



##### 3) requirements.txt

> pyton ์์๋ ํจํค์ง ์์กด์ฑ์ ๊ณต์ ํ  ๋ ๊ฐ์ฅ ๋ฒ์ฉ์ ์ผ๋ก ์ฌ์ฉ๋๋ ๊ฒ์ด requrements.txt ์ด๋ค. ํ์ฌ ํ์ด์ฌ ํ๊ฒฝ์์ ์ค์น๋ ํจํค์ง๋ค์ ์ ๋ฆฌํ ๋ ์๋์ ๋ช๋ น์ด๋ฅผ ์๋ ฅํ๋ค. 
>
> ```bash
> pip freeze > requirements.txt
> ```
>
> ๋ช๋ น์ด๋ฅผ ํตํด ์ค์น๋ ํจํค์ง๋ค์ด requirements.txt์ ๋์ด๋๊ณ  ์ด ํ์ผ์ ์ด์ฉํ์ฌ ํจํค์ง๋ค์ ์ค์นํ๊ณ ์ ํ ๋ ๋ค์๊ณผ ๊ฐ์ ๋ช๋ น์ด๋ฅผ ์๋ ฅํ๋ค. 
>
> ```bash
> pip install -r requirements.txt
> ```
>
> ![image-20221004145755239](../imges/Django CRUD/image-20221004145755239.png)



##### 4) ํ๋ก์ ํธ ์์ฑ

```bash
$  django-admin startproject pjt . 
```

![image-20221004151933282](../imges/Django CRUD/image-20221004151933282.png)

```bash
$ python manage.py runserver
```

![image-20221004152121134](../imges/Django CRUD/image-20221004152121134.png)

> * #####  settings.py ์์ ๋ค์๊ณผ ๊ฐ์ด ๋ด์ฉ ์์ ํ๊ธฐ : ํ๊ธ ๋ฒ์ 
>
> ![image-20221004152347648](../imges/Django CRUD/image-20221004152347648.png)
>
> ![image-20221004152406911](../imges/Django CRUD/image-20221004152406911.png)
>
> * ##### ์๋ฒ ๋ก๊ทธ ํ์ธํ๊ธฐ 
>
> ![image-20221004152707421](../imges/Django CRUD/image-20221004152707421.png)



##### 5) **Articles** app **์์ฑ**

```bash
$ python manage.py startapp articles
```

![image-20221004153415436](../imges/Django CRUD/image-20221004153415436.png)

![image-20221004153754230](../imges/Django CRUD/image-20221004153754230.png)

---

```python
pjt URL์ ๊ตฌ์ฑ 

'urlpatterns' ๋ชฉ๋ก์ URL์ views๋ก ๋ผ์ฐํํฉ๋๋ค. ์์ธํ ๋ด์ฉ์ ๋ค์์ ์ฐธ์กฐํ์ญ์์ค.:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
	
์ : 
Function views
	1. import๋ฅผ ์ถ๊ฐ : my_app ์ผ๋ก ๋ถํฐ views imort ํ๊ธฐ 
	2. urlpatterns์ URL ์ถ๊ฐ : path (''. views.home, name='home')
Class-based views
	1. import๋ฅผ ์ถ๊ฐ :other_app.views์์ Home ๊ฐ์ ธ์ค๊ธฐ 
	2. urlpatterns์ URL ์ถ๊ฐ : path('', Home.as_view(), name='home')
Including another URLconf
	1. include() ํจ์ ๊ฐ์ ธ์ค๊ธฐ : django.urls์์ ๊ฐ์ ธ์ค๊ธฐ ํฌํจ, ๊ฒฝ๋ก(path)
    2. urlpatterns์ URL ์ถ๊ฐ : path('blog/', include('blog.urls'))
```

![image-20221004154256124](../imges/Django CRUD/image-20221004154256124.png)

---



##### 5) pjt > urls.py 

> * ##### include๋ฅผ ํ๋ ์ด์ ๋  url ์ค์ ์ app๋จ์๋ก ํ๊ธฐ ์ํด์ ์งํํ๋ค. 

```python
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/".include("articles.urls")),
]
```

![image-20221004160508181](../imges/Django CRUD/image-20221004160508181.png)



##### 6) articles > urls.py ์์ฑ

```python
URL ์ค์ ์ app ๋จ์๋ก ํ๋ค ๋ ๋ฐ๋์ ๋ค์ด๊ฐ์ผ ํ๋ ๊ฒ
=> urlpatterns
```

![image-20221004161319547](../imges/Django CRUD/image-20221004161319547.png)

```python

# ํ์ํ๊ฑด urlpatterns ์ด์ง๋ง, ๋ค๋ฅธ ํ์ฉ๋ค์ ํ๊ธฐ ์ํด์ app_name = 'articles' ๋ฅผ ์ถ๊ฐ ์ค์ ์ ํด์ค๋ค. 
# urlpatterns ์์ ์๋ path๋ฅผ ์ฌ์ฉํ๊ธฐ ์ํด from django.urls import path ๋ฅผ ์์ฑํ๋ค. 

# ๊ฐ์ฅ ๊ธฐ๋ณธ ์ค์  

from django.urls import path

app_name = 'articles'

urlpatterns = []

```



---

* #### ํ๋ฆ ์ดํดํ๊ธฐ 

![image-20221004162208064](../imges/Django CRUD/image-20221004162208064.png)

---



![image-20221004162543002](../imges/Django CRUD/image-20221004162543002.png)



> ##### 1. ' ___ ' ๋ผ๋ ๊ฒฝ๋ก๋ก ๋ค์ด๊ฐ๋ฉด,  views.index ๋ผ๋ ํจ์๋ฅผ ์คํํ  ๊ฒ์ด๋ค. ๊ทธ๋ฆฌ๊ณ  ๊ทธ๊ฒ์ index๋ผ๋ ์ด๋ฆ์ผ๋ก ๋ถ๋ฅผ ๊ฒ์ด๋ค. 
>
> * ##### NameError : name 'views' is not defined
>
> ##### 2. from . import views
>
> * ##### AttributeError : module 'articles.views' has no attribute 'index'



##### 6) articles > views.py ํจ์ ์ ์ 

* ##### views ํ์ผ ๊ตฌ์ฑ 

![image-20221004164123258](../imges/Django CRUD/image-20221004164123258.png)

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "articles/index.html")
```



##### 7) Template ์์ฑ

![image-20221004164500057](../imges/Django CRUD/image-20221004164500057.png)

> ##### index.html

![image-20221004165054080](../imges/Django CRUD/image-20221004165054080.png)



---

* #### ๋ค์ ํ๋ฆ์ก๊ธฐ 

![image-20221004170150992](../imges/Django CRUD/image-20221004170150992.png)

![image-20221004170336033](../imges/Django CRUD/image-20221004170336033.png)

---



### <span style='background-color:#fff5b1'>ย  ย ๐ค CRUDย  ย </span>



#### 1. ๋ชจ๋ธ(๋ชจํ) ์ ์ํ๊ธฐ (DB ์คํค๋ง ์ค๊ณ)

---

![image-20221004173956589](../imges/Django CRUD/image-20221004173956589.png)

---

> ##### ์ด๋ค ๋ชจํ? ์์คํ ๊ธฐ๋ฐ์ ๋ชจํ 

> ##### UI(๊ธฐ๋ฅ) ์ ๋ฐ๋ผ์ DB๊ฐ ๊ฒฐ์ ๋๋ค. ์ฆ, UI์ DB๋ ๋ฐ์ ํ ๊ด๊ณ๋ฅผ ๊ฐ์ง ์ ๋ฐ์ ์๋ค. 

![image-20221004173325218](../imges/Django CRUD/image-20221004173325218.png)

![image-20221004173308218](../imges/Django CRUD/image-20221004173308218.png)

---



##### (1) ํด๋์ค ์ ์ 

![image-20221004174125273](../imges/Django CRUD/image-20221004174125273.png)



##### (2) ๋ง์ด๊ทธ๋ ์ด์ ํ์ผ ์์ฑ

```bash
$ python manage.py makemigrations
```

![image-20221004174154299](../imges/Django CRUD/image-20221004174154299.png)



##### (3) DB ๋ฐ์

```BASH
$ python manage.py migrate
```

![image-20221004174349138](../imges/Django CRUD/image-20221004174349138.png)



##### (4) DB ๋ฐ์ ํ์ธํ๊ธฐ 

```bash
$ python manage.py showmigrations
```

![image-20221004174902490](../imges/Django CRUD/image-20221004174902490.png)





### <span style='background-color:#fff5b1'>ย  ย  ๐ฅ CRUD ๊ธฐ๋ฅ ๊ตฌํ _ 01. ์์ฑย  ย  ย ย </span>



### 1. ๊ฒ์๊ธ ์์ฑ 

---

#### โญ ๋ด๊ฐ ์ด๋ ํ ๊ธฐ๋ฅ์ ๋ง๋ค๊ณ  ์ถ๋ค๋ฉด,

#### <span style='background-color: #ffdce0'>URL ์ mapping ๋๋ VIEW ํจ์๋  ๊ฐ๊ฐ 1๊ฐ๊ฐ ํ์ํ๋ค. </span>

#### 	๐ค WHY?  ํน์  URL์ ๊ฐ๊ฐ ๊ธฐ๋ฅ๋ค์ด ๋ค๋ฅด๊ธฐ ๋๋ฌธ์ด๋ค. 

---

![image-20221004180309872](../imges/Django CRUD/image-20221004180309872.png)

---

![image-20221004181330051](../imges/Django CRUD/image-20221004181330051.png)

> ##### ์์ฐ์ค๋ฝ๊ฒ ๊ฒ์๊ธ ์์ฑ์ด๋ผ๋ ๊ฒ์ ๋ง๋ค๊ณ  ์ถ๋ค๋ฉด ์ฒซ๋ฒ์งธ ์ฌ์ฉ์์๊ฒ HTML ์ ์ฃผ๋ ๊ธฐ๋ฅ๊ณผ ๋๋ฒ์งธ DB์ ์ ์ฅํ๋ ๊ธฐ๋ฅ์ ์๊ฐํด ๋ณผ ์ ์๋ค. ๋ฐ๋ผ์ 2๊ฐ์ URL๊ณผ 2๊ฐ์ VIEW ํจ์๊ฐ ๋ง๋ค์ด์ง๋ค. 
>
> ##### โญ ๋์ผํ URL์์ ์ฒ๋ฆฌํ  ์ ์๋ค๋ ์  ๋ฐ๋์ ๊ธฐ์ตํ๊ธฐ 



#### 1-1. HTML Form ์ ๊ณต

> ##### http://localhost:8000/articles/new ์ด๋ฏธ ์ค๊ณ๊ฐ ๋ ์ํ์์ ์์ฑ์ ํ๋ ๊ฒ!

> ##### ์ฌ์ฉ์๊ฐ INPUT๋ฅผ ์ฌ์ฉํ  ์ ์๋๋ก ์์ฑ 



##### (1) URL 

![image-20221004181726580](../imges/Django CRUD/image-20221004181726580.png)

##### (2) view

![image-20221004181900225](../imges/Django CRUD/image-20221004181900225.png)

##### (3) new.html ํ์ผ ์์ฑ

![image-20221004190929102](../imges/Django CRUD/image-20221004190929102.png)

![image-20221004190856139](../imges/Django CRUD/image-20221004190856139.png)



์ฌ์ฉ์๊ฐ INPUT๋ฅผ ์ฌ์ฉํ  ์ ์๋๋ก ์์ฑ 

#### ![image-20221004193229417](../imges/Django CRUD/image-20221004193229417.png)

#### 1-2. ์๋ ฅ๋ฐ์ ๋ฐ์ดํฐ ์ฒ๋ฆฌ 

> ##### http://localhost:8000/articles/create/ 

> ##### ์ฌ์ฉ์๋ก๋ถํฐ ๊ฐ์ ๋ฐ์์ ์ฒ๋ฆฌํ๋๋ก ์์ฑ 

![image-20221004222043082](../imges/Django CRUD/image-20221004222043082.png)

##### (1) URL 

![image-20221004222400199](../imges/Django CRUD/image-20221004222400199.png)



##### (2) view

![image-20221004222555901](../imges/Django CRUD/image-20221004222555901.png)

```python 
def create(request):
	pass
```

![image-20221004223240839](../imges/Django CRUD/image-20221004223240839.png)

![image-20221004223712185](../imges/Django CRUD/image-20221004223712185.png)



![image-20221004223906270](../imges/Django CRUD/image-20221004223906270.png)

##### (3) Articles ๋ผ๋ ํด๋์ค๋ models.py์ ์๋ ๋ชจ๋ธ์ด๋ค. 

![image-20221004224131054](../imges/Django CRUD/image-20221004224131054.png)



##### (4) ๊ฒ์๊ธ DB์ ์์ฑ ํ INDEX ํ์ด์ง๋ก redirect

> ##### redirect import ํ๊ธฐ 

![image-20221004224318033](../imges/Django CRUD/image-20221004224318033.png)



> ##### ๋ค์ index ๋ก ๋์๊ฐ์ค 
>
> ```python
> return redirect('articles:index')
> ```

![image-20221004224432346](../imges/Django CRUD/image-20221004224432346.png)



##### (5) ์์ฑ ๋ฒํผ ์์ฑ

![image-20221004225656648](../imges/Django CRUD/image-20221004225656648.png)

![image-20221004225728562](../imges/Django CRUD/image-20221004225728562.png)

![2022-10-04 22;58;26](../imges/Django CRUD/2022-10-04 22;58;26.gif)

---



### 2. ๊ฒ์๊ธ ๋ชฉ๋ก ๊ธฐ๋ฅ ๊ตฌํ 



#### 2-1. HTML Form ์ ๊ณต

#### โญ DB์์ ๊ฒ์๊ธ์ ๊ฐ์ ธ์์, template์ ์ ๋ฌ 

![image-20221004230355150](../imges/Django CRUD/image-20221004230355150.png)

![image-20221004230556892](../imges/Django CRUD/image-20221004230556892.png)



#### 2-2. index.html 

```html
<h1>๊ฒ์ํ</h1>
    <a href="{% url 'articles:new' %}">๊ธ์ฐ๊ธฐ</a>
    {% for article in articles %}
      <h3>{{ article.title }}</h3>
      <p>{{ article.created_at }} | {{ article.updated_at }}</p>
      <hr>
    {% endfor %}
```

![image-20221004231102664](../imges/Django CRUD/image-20221004231102664.png)

---

![image-20221004231859947](../imges/Django CRUD/image-20221004231859947.png)

---



#### 2-3. http://localhost:8000/articles/

![image-20221004232013259](../imges/Django CRUD/image-20221004232013259.png)



> ##### ๐ค ๋ง์ฝ ์ ์ผ ๋์ค์ ์์ฑํ๋ ๊ธ์ด ๊ฒ์ํ ๋ชฉ๋ก ์๋ก ๊ฐ์ ธ์ค๊ณ  ์ถ๋ค๋ฉด?  ๋ค์๊ณผ ๊ฐ์ด ์ฝ๋๋ฅผ ์์ฑํ๋ค. 

![image-20221004232335293](../imges/Django CRUD/image-20221004232335293.png)

![image-20221004232407674](../imges/Django CRUD/image-20221004232407674.png)



---

#### 2-3. ํ๋ฆ ์ ๋ฆฌ _ ๋ณ์ ์ด๋ฆ ์ฃผ์

##### (1) DB ์์ ๊ฐ์ ๊ฐ์ง๊ณ  ์จ๋ค. 

##### (2) Template์ context ๋ก ์ ๋ฌํ๋ค. 

##### (3) aricles(index.html)์ name ์ํฅ์ context ๋์๋๋ฆฌ key๊ฐ์ด๋ค. 

##### (4) `Article.objects.order_by('-pk')` ์ ์ฟผ๋ฆฌ์ (Article ๊ฐ์ฒด๋ฅผ ๊ฐ์ง) ์ด๋ค. 

![image-20221004233335179](../imges/Django CRUD/image-20221004233335179.png)

---



### <span style='background-color:#fff5b1'>   ๐ค GET, POSTย </span>



##### โผ GET  

> ##### The `GET` method requests a representation of the specified resource(Article). Requests using `GET` should only retrieve data. (  Article์ ์กฐํํ๋ค.  )
>
> (GET ๋ฉ์๋๋ ์ง์ ๋ ๋ฆฌ์์ค์ ํํ์ ์์ฒญํฉ๋๋ค. GET์ ์ฌ์ฉํ๋ ์์ฒญ์ ๋ฐ์ดํฐ๋ง ๊ฒ์ํด์ผ ํฉ๋๋ค. )



##### โผ POST

> #####  The `POST` method submits an entity to the specifited resource (Article), often causing a change in state or side effects on the server.
>
> ('POST' ๋ฉ์๋๋ ์ํฐํฐ๋ฅผ ์ง์ ๋ ๋ฆฌ์์ค์ ์ ์ถํ์ฌ ์ข์ข ์๋ฒ์ ์ํ ๋ณ๊ฒฝ์ด๋ ๋ถ์์ฉ์ ์ ๋ฐํฉ๋๋ค.)



#### 1-1. CSRF

> * ##### method="POST" ๋ฅผ ์ถ๊ฐํ ํ ๊ธ์ฐ๊ธฐ๋ฅผ ํตํด ๊ธ์ ์ถ๊ฐํ์๋ค. 
>
> * ##### ์ถ๊ฐ ํ CSRF ๊ฒ์ฆ์ ์คํจํ์ต๋๋ค. ๋ผ๋ ์ค๋ฅ๊ฐ ๋ฐ์ํ์๋ค. 

![image-20221005013159116](../imges/Django CRUD/image-20221005013159116.png)

```
Help 
์คํจ ์ด์ :
	CSRF ์ฟ ํค๊ฐ ์ค์ ๋์ง ์์์ต๋๋ค.
```

```
์ผ๋ฐ์ ์ผ๋ก ์ด๊ฒ์ ์ง์ ํ Cross Site Request Forgery๊ฐ ์๊ฑฐ๋ Django์ CSRF ๋ฉ์ปค๋์ฆ์ด ์ฌ๋ฐ๋ฅด๊ฒ ์ฌ์ฉ๋์ง ์์์ ๋ ๋ฐ์ํ  ์ ์์ต๋๋ค. POST ์์์ ๊ฒฝ์ฐ ๋ค์์ ํ์ธํด์ผ ํฉ๋๋ค.
```

> * ๊ทํ์ ๋ธ๋ผ์ฐ์ ๋ ์ฟ ํค๋ฅผ ํ์ฉํ๊ณ  ์์ต๋๋ค. 
> * view ํจ์๋ ํํ๋ฆฟ์ render ๋ฉ์๋์ ์์ฒญ์ ์ ๋ฌํฉ๋๋ค. 
> * ํํ๋ฆฟ์๋ ๋ด๋ถ URL์ ๋์์ผ๋ก ํ๋ ๊ฐ POST ์์ ๋ด๋ถ์ {% csrf_token %}  ํํ๋ฆฟ ํ๊ทธ๊ฐ ์์ต๋๋ค. 
> * CsrfViewMiddleware๋ฅผ ์ฌ์ฉํ์ง ์๋ ๊ฒฝ์ฐ SSRF_TOKEN ํํ๋ฆฟ ํ๊ทธ๋ฅผ ์ฌ์ฉํ๋ ๋ณด๊ธฐ์ POST ๋ฐ์ดํฐ๋ฅผ ํ์ฉํ๋ ๋ณด๊ธฐ์์ CSRF_PROTECT๋ฅผ ์ฌ์ฉํด์ผ ํฉ๋๋ค. 
> * ์์์ ์ ํจํ CSRF ํ ๊ทผ์ด ์์ต๋๋ค. ๋ค๋ฅธ ๋ธ๋ผ์ฐ์  ํญ์ ๋ก๊ทธ์ธ ํ๊ฑฐ๋ ๋ก๊ทธ์ธ ํ ๋ค๋ก ๋ฒํผ์ ๋๋ฅธ ํ ๋ก๊ทธ์ธ ํ ํ ํฐ์ด ์ํ๋๊ธฐ ๋๋์ ์์์ด ์๋ ํ์ด์ง๋ฅผ ๋ค์ ๋ก๋ํด์ผ ํ  ์ ์์ต๋๋ค.

```
Django ์ค์  ํ์ผ์ DEBUG=TRUE ๊ฐ ์๊ธฐ ๋๋ฌธ์ ์ด ํ์ด์ง์ ๋์๋ง ์น์์ด ํ์๋ฉ๋๋ค. 
FALSE๋ก ๋ณ๊ฒฝํ๋ฉด ์ด๊ธฐ ์ค๋ฅ ๋ฉ์์ง๋ง ํ์๋ฉ๋๋ค. 
CSRF_FAILURE_VIEW ์ค์ ์ ์ฌ์ฉํ์ฌ ์ด ํ์ด์ง๋ฅผ ์ฌ์ฉ์ ์ ์ ํ  ์ ์์ต๋๋ค. 
```



#### 1-2.  {% csrf_token %} 

> * ##### {% csrf_token %} ์ถ๊ฐํ์ฌ ๋ค์ ํ์ธํด๋ณธ ๊ฒฐ๊ณผ ๋ค์๊ณผ ๊ฐ์ ์ค๋ฅ ๋ฉ์์ง๋ฅผ ํ์ธ ํ  ์ ์๋ค. 

![image-20221005014900119](../imges/Django CRUD/image-20221005014900119.png)



> * ##### POST ๋ก ์์ฒญํ๊ฒ ๋๋ฉด ๊บผ๋ด๋ ๋ฐฉ๋ฒ์ด ๋ค๋ฅด๋ค. 

![image-20221005015051589](../imges/Django CRUD/image-20221005015051589.png)



> * #####  GET ๋ฅผ POST๋ก ์์ ํด์ฃผ๋ฉด ์ํ๋ ์ ๋ณด๋ฅผ GET ํ  ์ ์๋ค. 

![image-20221005015256012](../imges/Django CRUD/image-20221005015256012.png)



> * ##### ์์ฃผ ํฐ ๋ณํ : HTTP ์ฃผ์๊ฐ ๋ฐ๋์ง ์๋๋ค. 
>
> * ##### POST ์์ฒญ์ ์ฃผ์๋ก์ ๋ค์ด๊ฐ๋ ๊ฒ์ด ์๋, ์์ฒญ ๋ฉ์ธ์ง์ ๋ด๊ฒจ์ ์ ์ก์ด ๋๊ธฐ ๋๋ฌธ์ด๋ค. 

![image-20221005015421934](../imges/Django CRUD/image-20221005015421934.png)

![image-20221005015547840](../imges/Django CRUD/image-20221005015547840.png)



#### 1-3. URL ํ์ 

#### [developers.themoviedb](https://developers.themoviedb.org/3/movies/get-movie-reviews)

![image-20221005015943665](../imges/Django CRUD/image-20221005015943665.png)

##### ์ ์ฅํ๊ณ  ๊ธฐ๋กํ๋ ํ์(๋ก๊ทธ์ธ) => POST

![image-20221005020028456](../imges/Django CRUD/image-20221005020028456.png)

##### ์กฐํ ํ๋ ํ์(๊ฒ์ํ๋ ์ฐฝ) => GET



> * ##### ๋ง์ฝ, URL ํ์ ์ ๊ธฐ๋กํ๊ณ  ์ถ๋ค๋ฉด? 
>
>   * ##### POST/movies/123/score
>
>   * ##### ๋ฌด์กฐ๊ฑด ๋ฑ๋กํด์ผ ํ๋ค.  WHY? `POST` ๊ฐ ๋ฌ๋ ค ์๊ธฐ ๋๋ฌธ์ด๋ค. 
>
> * ##### ํ์  ์กฐํ 
>
>   * ##### GET/movie/123/score
>
>   * ##### ๋ฌด์กฐ๊ฑด ์กฐํํด์ผ ํ๋ค.  WHY? `GET` ์ด ๋ฌ๋ ค ์๊ธฐ ๋๋ฌธ์ด๋ค. 



---

#### 1-4. ํ๋ฆ ์ ๋ฆฌ 

##### (1) METHOD๋ฅผ POST๋ก ์ ์ํ๊ธฐ 

```HTML
<form action="{% url 'articles:create' %}" method="POST">
```

##### (2) {% csrf_token %} ๋ฐ๋์ ์์ฑํ๊ธฐ 

```HTML
<form action="{% url 'articles:create' %}" method="POST">
{% csrf_token %} 
```

##### (3) ๊ฐ์ ๋ฐ์ ๋ POST request๋ก ์์ฑํ๊ธฐ 

```python
def create(request):
    # ์ค์  DB์ ์ ์ฅํ๋ ๋ก์ง
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("articles:index")
```

---



### <span style='background-color:#fff5b1'>   ๐ค Django ModelFormย </span>



##### 1. input ํ๊ทธ์ required ์ถ๊ฐ 

![image-20221005021723575](../imges/Django CRUD/image-20221005021723575.png)



##### 2.  forms.py

> * ##### artice_form.as_P

![image-20221005023159697](../imges/Django CRUD/image-20221005023159697.png)

##### ![image-20221005024252371](../imges/Django CRUD/image-20221005024252371.png)



> ##### P ํ๊ทธ๋ก ๊ฐ์ธ์ ธ ์๋ LAVEL, ๊ทธ๋ฆฌ๊ณ  INPUT 



##### 3.  ์ ํจ์ฑ ๊ฒ์ฌ 

![image-20221005025746084](../imges/Django CRUD/image-20221005025746084.png)

![image-20221005025757951](../imges/Django CRUD/image-20221005025757951.png)



> ##### ๊ตฌ๊ธ ๋ก๊ทธ์ธ ์ฒ๋ผ form ์ ์ถ๊ฐํ ์ฝ๋์ ๊ฒฐ๊ณผ๋ฌผ์ ๋ค์๊ณผ ๊ฐ๋ค. 

![image-20221005030216806](../imges/Django CRUD/image-20221005030216806.png)



##### 4. ์ฝ๋ ํฉ์น๊ธฐ  

##### (1) new๋ฅผ ์์ ๊ณ , create ๊ฐ์ url ์์ ์ฒ๋ฆฌํ๋ค. 

##### (2) ๋ง์ฝ, request.method == 'POST' ๋ผ๋ฉด DB์ ์ ์ฅ์ ํ๋ค. 

##### (3) ๊ทธ๊ฒ ์๋๋ผ๋ฉด, ariticle_form = ArticleForm()

##### (4) ์ฝ๋๋ฅผ ํ๋๋ก ํฉ์ณค๋ค๋ฉด, index.html {% url 'articles:create' %} ๋ผ๊ณ  ๋ณ๊ฒฝํด์ค๋ค. 

##### (5) url ์์๋ path new ๋ฅผ ์์ ์ค๋ค. 

![image-20221005031537650](../imges/Django CRUD/image-20221005031537650.png)

##### 5.  ์ฝ๋ ์ํ ๊ตฌ๊ฐ 

##### (1) create ์คํํ์ ๋

##### (2) ๊ธ์ฐ๊ธฐ ๋ฒํผ์ ๋๋ ์ ๋ 

![image-20221005032304464](../imges/Django CRUD/image-20221005032304464.png)

##### (3) invalid 

![image-20221005032242448](../imges/Django CRUD/image-20221005032242448.png)



---



### <span style='background-color:#fff5b1'>   ๐ค ์์ธ ๋ณด๊ธฐย  ย </span>

> ##### ํน์ ํ ๊ธ์ ๋ณธ๋ค. 

> ##### http://localhost:8000/articles/create/ 

> ##### โญ ๋ฐ๋์ id ๊ฐ์ด ๋ค์ด๊ฐ์ผํ๋ค. http://localhost:8000/articles/<int:pk>/

#### โญ ํน์ ํ ๊ธ์ ๋ณธ๋ค? ์ฆ, DB์ ์๋ ์์ด๋ ๊ฐ์ URL์ ๋ฃ์ด์ค์ผํ๋ค. 



##### 1. URL 

![image-20221005033257734](../imges/Django CRUD/image-20221005033257734.png)

##### 2. VIEW

![image-20221005033551665](../imges/Django CRUD/image-20221005033551665.png)



##### 3. detail.html

![image-20221005033818103](../imges/Django CRUD/image-20221005033818103.png)



##### 4. URL (index.html)

![image-20221005034033925](../imges/Django CRUD/image-20221005034033925.png)



##### 5. ๊ฒฐ๊ณผ๋ฌผ ํ์ธ 

![image-20221005034155001](../imges/Django CRUD/image-20221005034155001.png)



---



### <span style='background-color:#fff5b1'>   ๐ค ์ญ์ ํ๊ธฐย </span>

> #####  . http://localhost:8000/articles/<int:pk>/delete/

> ##### ํน์ ํ ๊ธ์ ์ญ์ ํ๋ค. 

---



### <span style='background-color:#fff5b1'>   ๐ค ์์ ํ๊ธฐย </span>

> ##### ํน์ ํ ๊ธ์ ์์ ํ๋ค ๋ผ๋ ๊ฑด ์ฌ์ฉ์์๊ฒ ์์ ๋ ๊ธ์ ๋ฐ์์ ํน์ ํ ๊ธ์ ์์ ํ๋ค. 

> ##### ์ฌ์ฉ์์๊ฒ ์์ ํ  ์ ์๋ ์์์ ์ ๊ณตํ๊ณ  (GET), ํน์ ํ ๊ธ์ ์์ ํ๋ค. (POST)

> #####  http://localhost:8000/articles/<int:pk>/update/



#### โ ์ฌ์ฉ์์๊ฒ ์์ ํ  ์ ์๋ ์์์ ์ ๊ณตํ๊ณ  (GET)



##### 1. URL

![image-20221005034821847](../imges/Django CRUD/image-20221005034821847.png)



##### 2.  ์์ ํ๊ธฐ ๋ฒํผ ์์ฑ (detail.index)

> articles ์คํ 

![image-20221005035034049](../imges/Django CRUD/image-20221005035034049.png)



##### 3. view

![image-20221005035623893](../imges/Django CRUD/image-20221005035623893.png)

##### 4. update.html

#### โญ form ์์ ์ค์ํ 2๊ฐ์ง ์์ 

##### โญ input : name, value

##### โญ action : method (์ด๋ค ๋ฐฉ์์ผ๋ก)

![image-20221005040213494](../imges/Django CRUD/image-20221005040213494.png)

##### 5. ๊ธ์ ์์ ํ๊ธฐ ์ํด ์๋ ์๋ ๊ธ์ด ๋จ์์๊ฒ ํ๋ ค๋ฉด? 

![image-20221005040516317](../imges/Django CRUD/image-20221005040516317.png)

##### 6. Forbidden ์ค๋ฅ ๋ฐ์ 

![image-20221005040655232](../imges/Django CRUD/image-20221005040655232.png)

![image-20221005040805122](../imges/Django CRUD/image-20221005040805122.png)

> ##### csrf token  ์์ฑํ๊ธฐ 



#### โ ํน์ ํ ๊ธ์ ์์ ํ๋ค. (POST)



##### 1. POST : input ๊ฐ ๊ฐ์ ธ์์, ๊ฒ์ฆํ๊ณ , DB ์ ์ ์ฅ

![image-20221005041940387](../imges/Django CRUD/image-20221005041940387.png)

##### 2.  update VS create

![image-20221005042045306](../imges/Django CRUD/image-20221005042045306.png)



---



### ์ต์ข ์ ๋ฆฌ 

![image-20221005042820956](../imges/Django CRUD/image-20221005042820956.png)

![image-20221005043101761](../imges/Django CRUD/image-20221005043101761.png)

#### 1. GET ์์ฒญ์ผ ๋ ์ฒ๋ฆฌ ํ๋ฆ

#### 2. POST ์์ฒญ์ผ ๋ ์ฒ๋ฆฌ ํ๋ฆ

#### 3. VALID ํ  ๋ 

#### 4. INVALID ํ ๋ 