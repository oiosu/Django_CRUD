


# π‘ Django CRUD (νλ¦μ λ¦¬)

![image](https://user-images.githubusercontent.com/99783474/193910840-ec5db066-0cb1-44de-b210-e962da6c9e93.png)



---
<details>
<summary> 1) κ°μνκ²½ μ€μΉνκΈ° </summary>
<div markdown="1">

> **κ°μνκ²½ μ€μΉλ₯Ό μ νλ κ±ΈκΉ?  => ν¨ν€μ§λ₯Ό λ³λλ‘ κ°μ Έκ°κΈ° μν΄ μ€μΉνλ€.**

```bash
$ python -m venv venv
```
![image](https://user-images.githubusercontent.com/99783474/193910897-b0fa8431-76df-45b8-8f37-0e4bd8a8ef67.png)

* ##### ativate  μ€νμ΄ ν΅μ¬ 

```bash
$ source venv/Scripts/activate 
(venv)
```

</div>
</details>


---


<details>
<summary> 2) Django μ€μΉ </summary>
<div markdown="1">

```bash
$ pip install django==3.2.13
```

![image](https://user-images.githubusercontent.com/99783474/193911032-3ad9fcb1-aed5-485f-9117-a2171df119ee.png)

---



#### 3) requirements.txt

> pyton μμλ ν¨ν€μ§ μμ‘΄μ±μ κ³΅μ ν  λ κ°μ₯ λ²μ©μ μΌλ‘ μ¬μ©λλ κ²μ΄ requrements.txt μ΄λ€. νμ¬ νμ΄μ¬ νκ²½μμ μ€μΉλ ν¨ν€μ§λ€μ μ λ¦¬ν λ μλμ λͺλ Ήμ΄λ₯Ό μλ ₯νλ€. 
>
> ```bash
> pip freeze > requirements.txt
> ```
>
> λͺλ Ήμ΄λ₯Ό ν΅ν΄ μ€μΉλ ν¨ν€μ§λ€μ΄ requirements.txtμ λμ΄λκ³  μ΄ νμΌμ μ΄μ©νμ¬ ν¨ν€μ§λ€μ μ€μΉνκ³ μ ν λ λ€μκ³Ό κ°μ λͺλ Ήμ΄λ₯Ό μλ ₯νλ€. 
>
> ```bash
> pip install -r requirements.txt
> ```
>
> ![image](https://user-images.githubusercontent.com/99783474/193911078-ce3d207e-db14-4b17-bc3b-ad38767aa0b7.png)


</div>
</details>

---

<details>
<summary> 4) νλ‘μ νΈ μμ± </summary>
<div markdown="1">

```bash
$  django-admin startproject pjt . 
```

![image](https://user-images.githubusercontent.com/99783474/193911114-eafdb308-2bbf-4e68-b372-ce692cf0a901.png)

```bash
$ python manage.py runserver
```

![image](https://user-images.githubusercontent.com/99783474/193911187-588d5b6c-e75b-4af2-8eea-e66dfa910ccb.png)

> * #####  settings.py μμ λ€μκ³Ό κ°μ΄ λ΄μ© μμ νκΈ° : νκΈ λ²μ 
>
> ![image](https://user-images.githubusercontent.com/99783474/193911237-26f09f99-08ca-4396-9060-a4cee87e4a78.png)
>
> ![image-20221004152406911](../imges/Django CRUD/image-20221004152406911.png)
>
> * ##### μλ² λ‘κ·Έ νμΈνκΈ° 
>
> ![image](https://user-images.githubusercontent.com/99783474/193911266-9148f749-586d-4a44-becd-6a92e0bbe831.png)

</div>
</details>

---

<details>
<summary> 5) Articles app μμ±</summary>
<div markdown="1">

```bash
$ python manage.py startapp articles
```

![image](https://user-images.githubusercontent.com/99783474/193911320-979c59ec-8583-4a91-8c2a-a27f818036ac.png)

---

```python
pjt URLμ κ΅¬μ± 

'urlpatterns' λͺ©λ‘μ URLμ viewsλ‘ λΌμ°νν©λλ€. μμΈν λ΄μ©μ λ€μμ μ°Έμ‘°νμ­μμ€.:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
	
μ : 
Function views
	1. importλ₯Ό μΆκ° : my_app μΌλ‘ λΆν° views imort νκΈ° 
	2. urlpatternsμ URL μΆκ° : path (''. views.home, name='home')
Class-based views
	1. importλ₯Ό μΆκ° :other_app.viewsμμ Home κ°μ Έμ€κΈ° 
	2. urlpatternsμ URL μΆκ° : path('', Home.as_view(), name='home')
Including another URLconf
	1. include() ν¨μ κ°μ Έμ€κΈ° : django.urlsμμ κ°μ Έμ€κΈ° ν¬ν¨, κ²½λ‘(path)
    2. urlpatternsμ URL μΆκ° : path('blog/', include('blog.urls'))
```

#### π‘ pjt > urls.py 

> * ##### includeλ₯Ό νλ μ΄μ λ  url μ€μ μ appλ¨μλ‘ νκΈ° μν΄μ μ§ννλ€. 

```python
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/".include("articles.urls")),
]
```

![image](https://user-images.githubusercontent.com/99783474/193911402-287228f4-9f33-4f05-b3cd-00cd49b67e1a.png)



#### π‘ articles > urls.py μμ±

```python
URL μ€μ μ app λ¨μλ‘ νλ€ λ λ°λμ λ€μ΄κ°μΌ νλ κ²
=> urlpatterns
```

![image](https://user-images.githubusercontent.com/99783474/193911419-3f0e155a-017b-4a22-97e4-1e362328d03c.png)

```python
# νμνκ±΄ urlpatterns μ΄μ§λ§, λ€λ₯Έ νμ©λ€μ νκΈ° μν΄μ app_name = 'articles' λ₯Ό μΆκ° μ€μ μ ν΄μ€λ€. 
# urlpatterns μμ μλ pathλ₯Ό μ¬μ©νκΈ° μν΄ from django.urls import path λ₯Ό μμ±νλ€. 

# κ°μ₯ κΈ°λ³Έ μ€μ  

from django.urls import path

app_name = 'articles'

urlpatterns = []

```


![image](https://user-images.githubusercontent.com/99783474/193911490-e2271042-047f-4897-b367-3a6e3f312690.png)



> ##### 1. ' ___ ' λΌλ κ²½λ‘λ‘ λ€μ΄κ°λ©΄,  views.index λΌλ ν¨μλ₯Ό μ€νν  κ²μ΄λ€. κ·Έλ¦¬κ³  κ·Έκ²μ indexλΌλ μ΄λ¦μΌλ‘ λΆλ₯Ό κ²μ΄λ€. 
>
> * ##### NameError : name 'views' is not defined
>
> ##### 2. from . import views
>
> * ##### AttributeError : module 'articles.views' has no attribute 'index'


</div>
</details>


---

 * #### νλ¦ μ΄ν΄νκΈ° 

![image](https://user-images.githubusercontent.com/99783474/193911449-cd087cf0-d49d-4161-b1b4-880f6a93d48e.png)

---

<details>
<summary> 6) articles > views.py ν¨μ μ μ </summary>


<div markdown="1">

![image](https://user-images.githubusercontent.com/99783474/193911534-a063ba57-16b0-4a68-a274-ca1a426120bb.png)

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "articles/index.html") 
```

</div>
</details>

---


<details>
<summary>7) Template μμ±</summary>


<div markdown="1">


![image](https://user-images.githubusercontent.com/99783474/193911617-6e6fe526-d4a7-41a2-8712-0b7d10bef294.png)
> ##### index.html

![image](https://user-images.githubusercontent.com/99783474/193911651-a5b6769b-9ddc-47ef-86b7-28b59a5ac412.png)



</div>
</details>

---

* ### λ€μ νλ¦μ‘κΈ° 

<details>
<summary>νλ¦ μ λ¦¬</summary>
<div markdown="1">


![image](https://user-images.githubusercontent.com/99783474/193911685-d9a49569-4315-4f47-9857-64c4ad193210.png)

![image](https://user-images.githubusercontent.com/99783474/193911748-5d8968c2-2256-4af5-ab1c-a280bbce8cba.png)

</div>
</details>

---


## <span style='background-color:#fff5b1'>Β π€ CRUDΒ  Β </span>

<details>
<summary> 1. λͺ¨λΈ(λͺ¨ν) μ μνκΈ° (DB μ€ν€λ§ μ€κ³) </summary>
<div markdown="1">

---

![image](https://user-images.githubusercontent.com/99783474/193911805-1e45e5c7-9714-4613-89c3-d0d42f45faa9.png)

---

> ### μ΄λ€ λͺ¨ν? μμ€ν κΈ°λ°μ λͺ¨ν 

> ### UI(κΈ°λ₯) μ λ°λΌμ DBκ° κ²°μ λλ€. μ¦, UIμ DBλ λ°μ ν κ΄κ³λ₯Ό κ°μ§ μ λ°μ μλ€. 

![image](https://user-images.githubusercontent.com/99783474/193911837-deb9a5bd-8c3b-4a68-a428-63847cb5f804.png)


---



## (1) ν΄λμ€ μ μ 

![image](https://user-images.githubusercontent.com/99783474/193911878-09ccfa3b-b8c1-486d-bb46-9711f01c82ae.png)



## (2) λ§μ΄κ·Έλ μ΄μ νμΌ μμ±

```bash
$ python manage.py makemigrations
```

![image](https://user-images.githubusercontent.com/99783474/193911914-2f73f486-a7ae-4680-8e3c-4eb0f923dcf5.png)



## (3) DB λ°μ

```BASH
$ python manage.py migrate
```

![image](https://user-images.githubusercontent.com/99783474/193912040-d2bd750b-1cc0-463e-9cb2-9a9da86cba5f.png)



### (4) DB λ°μ νμΈνκΈ° 

```bash
$ python manage.py showmigrations
```
![image](https://user-images.githubusercontent.com/99783474/193912001-852140aa-08bc-493b-9392-7fb063846eb8.png)


</div>
</details>

---


### <span style='background-color:#fff5b1'>1. CRUD κΈ°λ₯ κ΅¬ν </span>


<details>
<summary>1. κ²μκΈ μμ± </summary>
<div markdown="1">

#### β­ λ΄κ° μ΄λ ν κΈ°λ₯μ λ§λ€κ³  μΆλ€λ©΄,

#### <span style='background-color: #ffdce0'>URL μ mapping λλ VIEW ν¨μλ  κ°κ° 1κ°κ° νμνλ€. </span>

#### 	π€ WHY?  νΉμ  URLμ κ°κ° κΈ°λ₯λ€μ΄ λ€λ₯΄κΈ° λλ¬Έμ΄λ€. 

---

![image](https://user-images.githubusercontent.com/99783474/193912239-92a29903-d69b-46ce-9fe7-454f73a5e562.png)

---

![image](https://user-images.githubusercontent.com/99783474/193912267-2d735deb-da5f-4374-a71d-8862273dabd3.png)

> ##### μμ°μ€λ½κ² κ²μκΈ μμ±μ΄λΌλ κ²μ λ§λ€κ³  μΆλ€λ©΄ μ²«λ²μ§Έ μ¬μ©μμκ² HTML μ μ£Όλ κΈ°λ₯κ³Ό λλ²μ§Έ DBμ μ μ₯νλ κΈ°λ₯μ μκ°ν΄ λ³Ό μ μλ€. λ°λΌμ 2κ°μ URLκ³Ό 2κ°μ VIEW ν¨μκ° λ§λ€μ΄μ§λ€. 
>
> ##### β­ λμΌν URLμμ μ²λ¦¬ν  μ μλ€λ μ  λ°λμ κΈ°μ΅νκΈ° 



#### 1-1. HTML Form μ κ³΅

> ##### http://localhost:8000/articles/new μ΄λ―Έ μ€κ³κ° λ μνμμ μμ±μ νλ κ²!

> ##### μ¬μ©μκ° INPUTλ₯Ό μ¬μ©ν  μ μλλ‘ μμ± 



##### (1) URL 

![image](https://user-images.githubusercontent.com/99783474/193912304-29959561-f52b-4a54-8c40-d428cabb9d2c.png)

##### (2) view

![image](https://user-images.githubusercontent.com/99783474/193912330-10396f7a-1c3b-49fd-87ab-e2db9c420fe4.png)

##### (3) new.html νμΌ μμ±

![image](https://user-images.githubusercontent.com/99783474/193912369-d7216c09-3c12-4a30-9057-46e429a36ff2.png)



μ¬μ©μκ° INPUTλ₯Ό μ¬μ©ν  μ μλλ‘ μμ± 

![image](https://user-images.githubusercontent.com/99783474/193912420-08e87d9b-f87c-4795-a14b-7ddf5bd65e68.png)

#### 1-2. μλ ₯λ°μ λ°μ΄ν° μ²λ¦¬ 

> ##### http://localhost:8000/articles/create/ 

> ##### μ¬μ©μλ‘λΆν° κ°μ λ°μμ μ²λ¦¬νλλ‘ μμ± 

![image](https://user-images.githubusercontent.com/99783474/193912479-9082095e-3e4b-4343-98ba-3da4a38720cd.png)

##### (1) URL 

![image](https://user-images.githubusercontent.com/99783474/193912537-8ecc5296-bd7c-4e1e-9147-374300b1e173.png)


##### (2) view

![image](https://user-images.githubusercontent.com/99783474/193912569-5596adb7-fc9f-44bd-83b5-3f01a80d5ab1.png)

```python 
def create(request):
	pass
```

![image](https://user-images.githubusercontent.com/99783474/193912616-af1e1d02-5468-4efa-9cd4-7c2f3e572375.png)

![image](https://user-images.githubusercontent.com/99783474/193912669-d952188d-8a3a-4fea-9e63-08cb8335e820.png)



![image](https://user-images.githubusercontent.com/99783474/193912700-165df1ca-fedf-4b58-826c-4c5eda83aa6d.png)

##### (3) Articles λΌλ ν΄λμ€λ models.pyμ μλ λͺ¨λΈμ΄λ€. 

![image](https://user-images.githubusercontent.com/99783474/193912734-0523e1b1-6e71-4b76-b354-6cc2aa211096.png)



##### (4) κ²μκΈ DBμ μμ± ν INDEX νμ΄μ§λ‘ redirect

> ##### redirect import νκΈ° 

![image](https://user-images.githubusercontent.com/99783474/193912761-9e6e995b-5778-421d-a515-d0ba3890e1a1.png)


> ##### λ€μ index λ‘ λμκ°μ€ 
>
> ```python
> return redirect('articles:index')
> ```

![image](https://user-images.githubusercontent.com/99783474/193912786-6e3a57a3-605a-4336-a04a-564cc39820de.png)



##### (5) μμ± λ²νΌ μμ±

![image](https://user-images.githubusercontent.com/99783474/193912844-91c3b128-25a0-451a-a013-7da18ab854bb.png)

</div>
</details>

---


<details>
<summary> 2. κ²μκΈ λͺ©λ‘ κΈ°λ₯ κ΅¬ν</summary>
<div markdown="1">

#### 2-1. HTML Form μ κ³΅

#### β­ DBμμ κ²μκΈμ κ°μ Έμμ, templateμ μ λ¬ 

![image](https://user-images.githubusercontent.com/99783474/193912889-38e07bbb-d5d4-484b-ba4a-dbedea89d651.png)



#### 2-2. index.html 

```html
<h1>κ²μν</h1>
    <a href="{% url 'articles:new' %}">κΈμ°κΈ°</a>
    {% for article in articles %}
      <h3>{{ article.title }}</h3>
      <p>{{ article.created_at }} | {{ article.updated_at }}</p>
      <hr>
    {% endfor %}
```
![image](https://user-images.githubusercontent.com/99783474/193912975-8dec2514-3c33-416d-8ea9-18ae0ed2157f.png)

---

![image](https://user-images.githubusercontent.com/99783474/193913000-703f6562-ecb2-4389-84b0-83cbbe5175c2.png)

---



#### 2-3. http://localhost:8000/articles/

![image](https://user-images.githubusercontent.com/99783474/193913038-a9f139e2-cee0-410a-8a47-1fe1d3a94890.png)



> ##### π€ λ§μ½ μ μΌ λμ€μ μμ±νλ κΈμ΄ κ²μν λͺ©λ‘ μλ‘ κ°μ Έμ€κ³  μΆλ€λ©΄?  λ€μκ³Ό κ°μ΄ μ½λλ₯Ό μμ±νλ€. 

![image](https://user-images.githubusercontent.com/99783474/193913058-c9a50d1e-ed18-4572-b690-9d2a667b7345.png)



---

#### 2-3. νλ¦ μ λ¦¬ _ λ³μ μ΄λ¦ μ£Όμ

##### (1) DB μμ κ°μ κ°μ§κ³  μ¨λ€. 

##### (2) Templateμ context λ‘ μ λ¬νλ€. 

##### (3) aricles(index.html)μ name μν₯μ context λμλλ¦¬ keyκ°μ΄λ€. 

##### (4) `Article.objects.order_by('-pk')` μ μΏΌλ¦¬μ (Article κ°μ²΄λ₯Ό κ°μ§) μ΄λ€. 

![image](https://user-images.githubusercontent.com/99783474/193913092-181d60f8-d692-4acf-b8c7-cd236f206a28.png)

</div>
</details>
 

---


### <span style='background-color:#fff5b1'>!!! GET, POSTΒ </span>

<details>
<summary>GET & POST</summary>
<div markdown="1">

#### βΌ GET  

> ##### The `GET` method requests a representation of the specified resource(Article). Requests using `GET` should only retrieve data. (  Articleμ μ‘°ννλ€.  )
>
> (GET λ©μλλ μ§μ λ λ¦¬μμ€μ ννμ μμ²­ν©λλ€. GETμ μ¬μ©νλ μμ²­μ λ°μ΄ν°λ§ κ²μν΄μΌ ν©λλ€. )



#### βΌ POST

> #####  The `POST` method submits an entity to the specifited resource (Article), often causing a change in state or side effects on the server.
>
> ('POST' λ©μλλ μν°ν°λ₯Ό μ§μ λ λ¦¬μμ€μ μ μΆνμ¬ μ’μ’ μλ²μ μν λ³κ²½μ΄λ λΆμμ©μ μ λ°ν©λλ€.)



### 1-1. CSRF

> * ##### method="POST" λ₯Ό μΆκ°ν ν κΈμ°κΈ°λ₯Ό ν΅ν΄ κΈμ μΆκ°νμλ€. 
>
> * ##### μΆκ° ν CSRF κ²μ¦μ μ€ν¨νμ΅λλ€. λΌλ μ€λ₯κ° λ°μνμλ€. 

![image](https://user-images.githubusercontent.com/99783474/193913152-9a32554a-8918-444c-98bd-6f5bb64cfe98.png)

```
Help 
μ€ν¨ μ΄μ :
	CSRF μΏ ν€κ° μ€μ λμ§ μμμ΅λλ€.
```

```
μΌλ°μ μΌλ‘ μ΄κ²μ μ§μ ν Cross Site Request Forgeryκ° μκ±°λ Djangoμ CSRF λ©μ»€λμ¦μ΄ μ¬λ°λ₯΄κ² μ¬μ©λμ§ μμμ λ λ°μν  μ μμ΅λλ€. POST μμμ κ²½μ° λ€μμ νμΈν΄μΌ ν©λλ€.
```

> * κ·νμ λΈλΌμ°μ λ μΏ ν€λ₯Ό νμ©νκ³  μμ΅λλ€. 
> * view ν¨μλ ννλ¦Ώμ render λ©μλμ μμ²­μ μ λ¬ν©λλ€. 
> * ννλ¦Ώμλ λ΄λΆ URLμ λμμΌλ‘ νλ κ° POST μμ λ΄λΆμ {% csrf_token %}  ννλ¦Ώ νκ·Έκ° μμ΅λλ€. 
> * CsrfViewMiddlewareλ₯Ό μ¬μ©νμ§ μλ κ²½μ° SSRF_TOKEN ννλ¦Ώ νκ·Έλ₯Ό μ¬μ©νλ λ³΄κΈ°μ POST λ°μ΄ν°λ₯Ό νμ©νλ λ³΄κΈ°μμ CSRF_PROTECTλ₯Ό μ¬μ©ν΄μΌ ν©λλ€. 
> * μμμ μ ν¨ν CSRF ν κ·Όμ΄ μμ΅λλ€. λ€λ₯Έ λΈλΌμ°μ  ν­μ λ‘κ·ΈμΈ νκ±°λ λ‘κ·ΈμΈ ν λ€λ‘ λ²νΌμ λλ₯Έ ν λ‘κ·ΈμΈ ν ν ν°μ΄ μνλκΈ° λλμ μμμ΄ μλ νμ΄μ§λ₯Ό λ€μ λ‘λν΄μΌ ν  μ μμ΅λλ€.

```
Django μ€μ  νμΌμ DEBUG=TRUE κ° μκΈ° λλ¬Έμ μ΄ νμ΄μ§μ λμλ§ μΉμμ΄ νμλ©λλ€. 
FALSEλ‘ λ³κ²½νλ©΄ μ΄κΈ° μ€λ₯ λ©μμ§λ§ νμλ©λλ€. 
CSRF_FAILURE_VIEW μ€μ μ μ¬μ©νμ¬ μ΄ νμ΄μ§λ₯Ό μ¬μ©μ μ μ ν  μ μμ΅λλ€. 
```



### 1-2.  {% csrf_token %} 

> * ##### {% csrf_token %} μΆκ°νμ¬ λ€μ νμΈν΄λ³Έ κ²°κ³Ό λ€μκ³Ό κ°μ μ€λ₯ λ©μμ§λ₯Ό νμΈ ν  μ μλ€. 

![image](https://user-images.githubusercontent.com/99783474/193913185-29b49074-f15b-4378-8b9f-5fc3baf7b667.png)



> * #### POST λ‘ μμ²­νκ² λλ©΄ κΊΌλ΄λ λ°©λ²μ΄ λ€λ₯΄λ€. 

![image](https://user-images.githubusercontent.com/99783474/193913219-b746a30a-b35f-4d57-a50c-94af49f01ade.png)



> * ####  GET λ₯Ό POSTλ‘ μμ ν΄μ£Όλ©΄ μνλ μ λ³΄λ₯Ό GET ν  μ μλ€. 

![image](https://user-images.githubusercontent.com/99783474/193913273-69cfe082-166c-47f3-8014-7166ad97a665.png)



> * #### μμ£Ό ν° λ³ν : HTTP μ£Όμκ° λ°λμ§ μλλ€. 
>
> * #### POST μμ²­μ μ£Όμλ‘μ λ€μ΄κ°λ κ²μ΄ μλ, μμ²­ λ©μΈμ§μ λ΄κ²¨μ μ μ‘μ΄ λκΈ° λλ¬Έμ΄λ€. 

![image](https://user-images.githubusercontent.com/99783474/193913308-d544ab2c-2ca2-4cf3-bc19-03c075b0f792.png)



### 1-3. URL νμ 

#### [developers.themoviedb](https://developers.themoviedb.org/3/movies/get-movie-reviews)


![image](https://user-images.githubusercontent.com/99783474/193913344-ce21d8bc-fef6-41be-8f5c-b05d1c528e13.png)




> * ##### λ§μ½, URL νμ μ κΈ°λ‘νκ³  μΆλ€λ©΄? 
>
>   * ##### POST/movies/123/score
>
>   * ##### λ¬΄μ‘°κ±΄ λ±λ‘ν΄μΌ νλ€.  WHY? `POST` κ° λ¬λ € μκΈ° λλ¬Έμ΄λ€. 
>
> * ##### νμ  μ‘°ν 
>
>   * ##### GET/movie/123/score
>
>   * ##### λ¬΄μ‘°κ±΄ μ‘°νν΄μΌ νλ€.  WHY? `GET` μ΄ λ¬λ € μκΈ° λλ¬Έμ΄λ€. 



---

### 1-4. νλ¦ μ λ¦¬ 

#### (1) METHODλ₯Ό POSTλ‘ μ μνκΈ° 

```HTML
<form action="{% url 'articles:create' %}" method="POST">
```

#### (2) {% csrf_token %} λ°λμ μμ±νκΈ° 

```HTML
<form action="{% url 'articles:create' %}" method="POST">
{% csrf_token %} 
```

#### (3) κ°μ λ°μ λ POST requestλ‘ μμ±νκΈ° 

```python
def create(request):
    # μ€μ  DBμ μ μ₯νλ λ‘μ§
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("articles:index")
```

</div>
</details>



---



### <span style='background-color:#fff5b1'> 2. Django ModelFormΒ </span>


<details>
<summary>MODELFORM</summary>
<div markdown="1">

#### 1. input νκ·Έμ required μΆκ° 

![image](https://user-images.githubusercontent.com/99783474/193913422-6c3fb9f1-0923-4d59-80e8-7c69238c04d1.png)



#### 2.  forms.py

> * ##### artice_form.as_P

![image](https://user-images.githubusercontent.com/99783474/193913451-4ea7ea8f-5602-4508-ba28-6914bdcaf9f3.png)


![image](https://user-images.githubusercontent.com/99783474/193913483-5fd068c4-c55d-4111-8241-ff6d20a8adec.png)


> ##### P νκ·Έλ‘ κ°μΈμ Έ μλ LAVEL, κ·Έλ¦¬κ³  INPUT 



#### 3.  μ ν¨μ± κ²μ¬ 

![image](https://user-images.githubusercontent.com/99783474/193913540-0326202a-be6a-48da-bcd5-236a4ae74f32.png)

![image](https://user-images.githubusercontent.com/99783474/193913568-14200183-b29f-439d-ac45-1fc3a1cea2ad.png)



> #### κ΅¬κΈ λ‘κ·ΈμΈ μ²λΌ form μ μΆκ°ν μ½λμ κ²°κ³Όλ¬Όμ λ€μκ³Ό κ°λ€. 

![image](https://user-images.githubusercontent.com/99783474/193913601-4fc35945-d491-48b8-a737-18a95c591260.png)



#### 4. μ½λ ν©μΉκΈ°  

#### (1) newλ₯Ό μμ κ³ , create κ°μ url μμ μ²λ¦¬νλ€. 

#### (2) λ§μ½, request.method == 'POST' λΌλ©΄ DBμ μ μ₯μ νλ€. 

#### (3) κ·Έκ² μλλΌλ©΄, ariticle_form = ArticleForm()

#### (4) μ½λλ₯Ό νλλ‘ ν©μ³€λ€λ©΄, index.html {% url 'articles:create' %} λΌκ³  λ³κ²½ν΄μ€λ€. 

#### (5) url μμλ path new λ₯Ό μμ μ€λ€. 

![image](https://user-images.githubusercontent.com/99783474/193913643-e6173a4f-df5f-432c-bee8-065f7763910c.png)

#### 5.  μ½λ μν κ΅¬κ° 

#### (1) create μ€ννμ λ

#### (2) κΈμ°κΈ° λ²νΌμ λλ μ λ 

![image](https://user-images.githubusercontent.com/99783474/193913678-e045998b-7b89-4099-b1bc-1e21a0d4dbf5.png)

#### (3) invalid 

![image](https://user-images.githubusercontent.com/99783474/193913708-36f80b49-6c0f-4374-84ed-40b4b6e2d454.png)


</div>
</details>


---


### <span style='background-color:#fff5b1'> 3. μμΈ λ³΄κΈ°Β  Β </span>

> ##### νΉμ ν κΈμ λ³Έλ€. 

> ##### http://localhost:8000/articles/create/ 

> ##### β­ λ°λμ id κ°μ΄ λ€μ΄κ°μΌνλ€. http://localhost:8000/articles/<int:pk>/

#### β­ νΉμ ν κΈμ λ³Έλ€? μ¦, DBμ μλ μμ΄λ κ°μ URLμ λ£μ΄μ€μΌνλ€. 

<details>
<summary>DETAIL</summary>
<div markdown="1">

#### 1. URL 

![image](https://user-images.githubusercontent.com/99783474/193913878-19433239-331c-4ddb-9d11-d43645cc6084.png)

#### 2. VIEW
![image](https://user-images.githubusercontent.com/99783474/193913916-9cb27aab-c68b-4f8f-8ad8-f279d67458d3.png)



#### 3. detail.html

![image](https://user-images.githubusercontent.com/99783474/193913945-ee16e365-4ac9-433d-9b21-ace5edaa9033.png)



#### 4. URL (index.html)

![image](https://user-images.githubusercontent.com/99783474/193913975-57903eb4-8948-4f87-a885-17b0045af2ea.png)


#### 5. κ²°κ³Όλ¬Ό νμΈ 

![image](https://user-images.githubusercontent.com/99783474/193913995-cb92d52a-56ba-4a55-a7ec-0e60e8c40de1.png)


</div>
</details>


---



### <span style='background-color:#fff5b1'>4. μ­μ νκΈ°Β </span>

<details>
<summary>DELETE</summary>
<div markdown="1">

> #####  . http://localhost:8000/articles/<int:pk>/delete/

> ##### νΉμ ν κΈμ μ­μ νλ€. 

</div>
</details>

---


### <span style='background-color:#fff5b1'> 5. μμ νκΈ°Β </span>

<details>
<summary>EDIT</summary>
<div markdown="1">

> ##### νΉμ ν κΈμ μμ νλ€ λΌλ κ±΄ μ¬μ©μμκ² μμ λ κΈμ λ°μμ νΉμ ν κΈμ μμ νλ€. 

> ##### μ¬μ©μμκ² μμ ν  μ μλ μμμ μ κ³΅νκ³  (GET), νΉμ ν κΈμ μμ νλ€. (POST)

> #####  http://localhost:8000/articles/<int:pk>/update/



### β μ¬μ©μμκ² μμ ν  μ μλ μμμ μ κ³΅νκ³  (GET)



#### 1. URL

![image](https://user-images.githubusercontent.com/99783474/193914186-0374224e-d428-4fa5-b4b0-404209d0cbfe.png)



#### 2.  μμ νκΈ° λ²νΌ μμ± (detail.index)

> articles μ€ν 

![image](https://user-images.githubusercontent.com/99783474/193914236-8e85ee9d-7c46-4903-97b5-4db205253b7e.png)



#### 3. view

![image](https://user-images.githubusercontent.com/99783474/193914268-cfd92edb-0dbb-40c8-b5fa-3331dc479792.png)

#### 4. update.html

#### β­ form μμ μ€μν 2κ°μ§ μμ 

##### β­ input : name, value

##### β­ action : method (μ΄λ€ λ°©μμΌλ‘)

![image](https://user-images.githubusercontent.com/99783474/193914296-b8bd4072-8757-453f-9603-a653b6dda5c5.png)

#### 5. κΈμ μμ νκΈ° μν΄ μλ μλ κΈμ΄ λ¨μμκ² νλ €λ©΄? 

![image](https://user-images.githubusercontent.com/99783474/193914319-54e408f6-ecd3-40cf-aeb5-071fcf32a21e.png)

#### 6. Forbidden μ€λ₯ λ°μ 

![image](https://user-images.githubusercontent.com/99783474/193914357-80f3a4a4-dc1d-45d6-a0a6-2d17adc8f14f.png)

> ##### csrf token  μμ±νκΈ° 



### β νΉμ ν κΈμ μμ νλ€. (POST)



#### 1. POST : input κ° κ°μ Έμμ, κ²μ¦νκ³ , DB μ μ μ₯

![image](https://user-images.githubusercontent.com/99783474/193914389-7206dad3-a52b-486a-819a-3b8fe935dbb5.png)

#### 2.  update VS create

![image](https://user-images.githubusercontent.com/99783474/193914425-6676bd16-6b9a-4dc6-aef7-42225ec9b953.png)

</div>
</details>


---


### π± μ΅μ’ μ λ¦¬ 

<details>
<summary>νλ¦ μ λ¦¬</summary>
<div markdown="1">

![image](https://user-images.githubusercontent.com/99783474/193914453-2f5ad025-5b7e-47b8-9233-8c103fd8ff2c.png)

![image](https://user-images.githubusercontent.com/99783474/193914478-f42294fd-e3ba-470f-9130-98c3855e8927.png)

#### 1. GET μμ²­μΌ λ μ²λ¦¬ νλ¦

#### 2. POST μμ²­μΌ λ μ²λ¦¬ νλ¦

#### 3. VALID ν  λ 

#### 4. INVALID ν λ 

</div>
</details>

---
---





