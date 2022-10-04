# Django CRUD 

![image](https://user-images.githubusercontent.com/99783474/193910840-ec5db066-0cb1-44de-b210-e962da6c9e93.png)



---



### <span style='background-color:#fff5b1'>   🐣 CRUD   </span>



##### 1) 가상환경 설치하기 

> ##### 가상환경 설치를 왜 하는 걸까?  => 패키지를 별도로 가져가기 위해 설치한다. 

```bash
$ python -m venv venv
```
![image](https://user-images.githubusercontent.com/99783474/193910897-b0fa8431-76df-45b8-8f37-0e4bd8a8ef67.png)

* ##### ativate  실행이 핵심 

```bash
$ source venv/Scripts/activate 
(venv)
```



##### 2) Django 설치 

```bash
$ pip install django==3.2.13
```

![image](https://user-images.githubusercontent.com/99783474/193911032-3ad9fcb1-aed5-485f-9117-a2171df119ee.png)



##### 3) requirements.txt

> pyton 에서는 패키지 의존성을 공유할 떄 가장 범용적으로 사용되는 것이 requrements.txt 이다. 현재 파이썬 환경에서 설치된 패키지들을 정리할땐 아래의 명령어를 입력한다. 
>
> ```bash
> pip freeze > requirements.txt
> ```
>
> 명령어를 통해 설치된 패키지들이 requirements.txt에 나열되고 이 파일을 이용하여 패키지들을 설치하고자 할때 다음과 같은 명령어를 입력한다. 
>
> ```bash
> pip install -r requirements.txt
> ```
>
> ![image](https://user-images.githubusercontent.com/99783474/193911078-ce3d207e-db14-4b17-bc3b-ad38767aa0b7.png)



##### 4) 프로젝트 생성

```bash
$  django-admin startproject pjt . 
```

![image](https://user-images.githubusercontent.com/99783474/193911114-eafdb308-2bbf-4e68-b372-ce692cf0a901.png)

```bash
$ python manage.py runserver
```

![image](https://user-images.githubusercontent.com/99783474/193911187-588d5b6c-e75b-4af2-8eea-e66dfa910ccb.png)

> * #####  settings.py 에서 다음과 같이 내용 수정하기 : 한글 버전
>
> ![image](https://user-images.githubusercontent.com/99783474/193911237-26f09f99-08ca-4396-9060-a4cee87e4a78.png)
>
> ![image-20221004152406911](../imges/Django CRUD/image-20221004152406911.png)
>
> * ##### 서버 로그 확인하기 
>
> ![image](https://user-images.githubusercontent.com/99783474/193911266-9148f749-586d-4a44-becd-6a92e0bbe831.png)



##### 5) **Articles** app **생성**

```bash
$ python manage.py startapp articles
```

![image](https://user-images.githubusercontent.com/99783474/193911320-979c59ec-8583-4a91-8c2a-a27f818036ac.png)

---

```python
pjt URL의 구성 

'urlpatterns' 목록은 URL을 views로 라우팅합니다. 자세한 내용은 다음을 참조하십시오.:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
	
예 : 
Function views
	1. import를 추가 : my_app 으로 부터 views imort 하기 
	2. urlpatterns에 URL 추가 : path (''. views.home, name='home')
Class-based views
	1. import를 추가 :other_app.views에서 Home 가져오기 
	2. urlpatterns에 URL 추가 : path('', Home.as_view(), name='home')
Including another URLconf
	1. include() 함수 가져오기 : django.urls에서 가져오기 포함, 경로(path)
    2. urlpatterns에 URL 추가 : path('blog/', include('blog.urls'))
```

![image](https://user-images.githubusercontent.com/99783474/193911362-e771be78-0efd-40f0-ac4a-df934b321f97.png)

---



##### 5) pjt > urls.py 

> * ##### include를 하는 이유는  url 설정을 app단위로 하기 위해서 진행한다. 

```python
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/".include("articles.urls")),
]
```

![image](https://user-images.githubusercontent.com/99783474/193911402-287228f4-9f33-4f05-b3cd-00cd49b67e1a.png)



##### 6) articles > urls.py 생성

```python
URL 설정을 app 단위로 했들 때 반드시 들어가야 하는 것
=> urlpatterns
```

![image](https://user-images.githubusercontent.com/99783474/193911419-3f0e155a-017b-4a22-97e4-1e362328d03c.png)

```python
# 필요한건 urlpatterns 이지만, 다른 활용들을 하기 위해서 app_name = 'articles' 를 추가 설정을 해준다. 
# urlpatterns 안에 있는 path를 사용하기 위해 from django.urls import path 를 작성한다. 

# 가장 기본 설정 

from django.urls import path

app_name = 'articles'

urlpatterns = []

```



---

* #### 흐름 이해하기 

![image](https://user-images.githubusercontent.com/99783474/193911449-cd087cf0-d49d-4161-b1b4-880f6a93d48e.png)

---



![image](https://user-images.githubusercontent.com/99783474/193911490-e2271042-047f-4897-b367-3a6e3f312690.png)



> ##### 1. ' ___ ' 라는 경로로 들어가면,  views.index 라는 함수를 실행할 것이다. 그리고 그것을 index라는 이름으로 부를 것이다. 
>
> * ##### NameError : name 'views' is not defined
>
> ##### 2. from . import views
>
> * ##### AttributeError : module 'articles.views' has no attribute 'index'



##### 6) articles > views.py 함수 정의 

* ##### views 파일 구성 

![image](https://user-images.githubusercontent.com/99783474/193911534-a063ba57-16b0-4a68-a274-ca1a426120bb.png)

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "articles/index.html")
```



##### 7) Template 생성

![image](https://user-images.githubusercontent.com/99783474/193911617-6e6fe526-d4a7-41a2-8712-0b7d10bef294.png)
> ##### index.html

![image](https://user-images.githubusercontent.com/99783474/193911651-a5b6769b-9ddc-47ef-86b7-28b59a5ac412.png)



---

* #### 다시 흐름잡기 

![image](https://user-images.githubusercontent.com/99783474/193911685-d9a49569-4315-4f47-9857-64c4ad193210.png)

![image](https://user-images.githubusercontent.com/99783474/193911748-5d8968c2-2256-4af5-ab1c-a280bbce8cba.png)

---



### <span style='background-color:#fff5b1'>   🐤 CRUD   </span>



#### 1. 모델(모형) 정의하기 (DB 스키마 설계)

---

![image](https://user-images.githubusercontent.com/99783474/193911805-1e45e5c7-9714-4613-89c3-d0d42f45faa9.png)

---

> ##### 어떤 모형? 시스템 기반의 모형 

> ##### UI(기능) 에 따라서 DB가 결정된다. 즉, UI와 DB는 밀접한 관계를 가질 수 밖에 없다. 

![image](https://user-images.githubusercontent.com/99783474/193911837-deb9a5bd-8c3b-4a68-a428-63847cb5f804.png)


---



##### (1) 클래스 정의 

![image](https://user-images.githubusercontent.com/99783474/193911878-09ccfa3b-b8c1-486d-bb46-9711f01c82ae.png)



##### (2) 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations
```

![image](https://user-images.githubusercontent.com/99783474/193911914-2f73f486-a7ae-4680-8e3c-4eb0f923dcf5.png)



##### (3) DB 반영

```BASH
$ python manage.py migrate
```

![image](https://user-images.githubusercontent.com/99783474/193912040-d2bd750b-1cc0-463e-9cb2-9a9da86cba5f.png)



##### (4) DB 반영 확인하기 

```bash
$ python manage.py showmigrations
```
![image](https://user-images.githubusercontent.com/99783474/193912001-852140aa-08bc-493b-9392-7fb063846eb8.png)





### <span style='background-color:#fff5b1'>    🐥 CRUD 기능 구현 _ 01. 생성      </span>



### 1. 게시글 생성 

---

#### ⭐ 내가 어떠한 기능을 만들고 싶다면,

#### <span style='background-color: #ffdce0'>URL 에 mapping 되는 VIEW 함수는  각각 1개가 필요하다. </span>

#### 	🤔 WHY?  특정 URL의 각각 기능들이 다르기 때문이다. 

---

![image](https://user-images.githubusercontent.com/99783474/193912239-92a29903-d69b-46ce-9fe7-454f73a5e562.png)

---

![image](https://user-images.githubusercontent.com/99783474/193912267-2d735deb-da5f-4374-a71d-8862273dabd3.png)

> ##### 자연스럽게 게시글 생성이라는 것을 만들고 싶다면 첫번째 사용자에게 HTML 을 주는 기능과 두번째 DB에 저장하는 기능을 생각해 볼 수 있다. 따라서 2개의 URL과 2개의 VIEW 함수가 만들어진다. 
>
> ##### ⭐ 동일한 URL에서 처리할 수 없다는 점 반드시 기억하기 



#### 1-1. HTML Form 제공

> ##### http://localhost:8000/articles/new 이미 설계가 된 상태에서 작성을 하는 것!

> ##### 사용자가 INPUT를 사용할 수 있도록 완성 



##### (1) URL 

![image](https://user-images.githubusercontent.com/99783474/193912304-29959561-f52b-4a54-8c40-d428cabb9d2c.png)

##### (2) view

![image](https://user-images.githubusercontent.com/99783474/193912330-10396f7a-1c3b-49fd-87ab-e2db9c420fe4.png)

##### (3) new.html 파일 생성

![image](https://user-images.githubusercontent.com/99783474/193912369-d7216c09-3c12-4a30-9057-46e429a36ff2.png)



사용자가 INPUT를 사용할 수 있도록 완성 

![image](https://user-images.githubusercontent.com/99783474/193912420-08e87d9b-f87c-4795-a14b-7ddf5bd65e68.png)

#### 1-2. 입력받은 데이터 처리 

> ##### http://localhost:8000/articles/create/ 

> ##### 사용자로부터 값을 받아서 처리하도록 완성 

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

##### (3) Articles 라는 클래스는 models.py에 있는 모델이다. 

![image](https://user-images.githubusercontent.com/99783474/193912734-0523e1b1-6e71-4b76-b354-6cc2aa211096.png)



##### (4) 게시글 DB에 생성 후 INDEX 페이지로 redirect

> ##### redirect import 하기 

![image](https://user-images.githubusercontent.com/99783474/193912761-9e6e995b-5778-421d-a515-d0ba3890e1a1.png)


> ##### 다시 index 로 돌아가줘 
>
> ```python
> return redirect('articles:index')
> ```

![image](https://user-images.githubusercontent.com/99783474/193912786-6e3a57a3-605a-4336-a04a-564cc39820de.png)



##### (5) 작성 버튼 생성

![image](https://user-images.githubusercontent.com/99783474/193912844-91c3b128-25a0-451a-a013-7da18ab854bb.png)

---



### 2. 게시글 목록 기능 구현 



#### 2-1. HTML Form 제공

#### ⭐ DB에서 게시글을 가져와서, template에 전달 

![image](https://user-images.githubusercontent.com/99783474/193912889-38e07bbb-d5d4-484b-ba4a-dbedea89d651.png)



#### 2-2. index.html 

```html
<h1>게시판</h1>
    <a href="{% url 'articles:new' %}">글쓰기</a>
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



> ##### 🤔 만약 제일 나중에 작성했던 글이 게시판 목록 위로 가져오고 싶다면?  다음과 같이 코드를 작성한다. 

![image](https://user-images.githubusercontent.com/99783474/193913058-c9a50d1e-ed18-4572-b690-9d2a667b7345.png)



---

#### 2-3. 흐름 정리 _ 변수 이름 주의

##### (1) DB 에서 값을 가지고 온다. 

##### (2) Template에 context 로 전달한다. 

##### (3) aricles(index.html)의 name 영향은 context 딕셔너리 key값이다. 

##### (4) `Article.objects.order_by('-pk')` 은 쿼리셋 (Article 객체를 가진) 이다. 

![image](https://user-images.githubusercontent.com/99783474/193913092-181d60f8-d692-4acf-b8c7-cd236f206a28.png)

---



### <span style='background-color:#fff5b1'>   🐤 GET, POST </span>



##### ◼ GET  

> ##### The `GET` method requests a representation of the specified resource(Article). Requests using `GET` should only retrieve data. (  Article을 조회한다.  )
>
> (GET 메서드는 지정된 리소스의 표현을 요청합니다. GET을 사용하는 요청은 데이터만 검색해야 합니다. )



##### ◼ POST

> #####  The `POST` method submits an entity to the specifited resource (Article), often causing a change in state or side effects on the server.
>
> ('POST' 메서드는 엔터티를 지정된 리소스에 제출하여 종종 서버의 상태 변경이나 부작용을 유발합니다.)



#### 1-1. CSRF

> * ##### method="POST" 를 추가한 후 글쓰기를 통해 글을 추가하였다. 
>
> * ##### 추가 후 CSRF 검증에 실패했습니다. 라는 오류가 발생하였다. 

![image](https://user-images.githubusercontent.com/99783474/193913152-9a32554a-8918-444c-98bd-6f5bb64cfe98.png)

```
Help 
실패 이유:
	CSRF 쿠키가 설정되지 않았습니다.
```

```
일반적으로 이것은 진정한 Cross Site Request Forgery가 있거나 Django의 CSRF 메커니즘이 올바르게 사용되지 않았을 때 발생할 수 있습니다. POST 양식의 경우 다음을 확인해야 합니다.
```

> * 귀하의 브라우저는 쿠키를 허용하고 있습니다. 
> * view 함수는 템플릿의 render 메소드에 요청을 전달합니다. 
> * 템플릿에는 내부 URL을 대상으로 하는 각 POST 양식 내부에 {% csrf_token %}  템플릿 태그가 있습니다. 
> * CsrfViewMiddleware를 사용하지 않는 경우 SSRF_TOKEN 템플릿 태그를 사용하는 보기와 POST 데이터를 허용하는 보기에서 CSRF_PROTECT를 사용해야 합니다. 
> * 양식에 유효한 CSRF 토근이 있습니다. 다른 브라우저 탭에 로그인 하거나 로그인 후 뒤로 버튼을 누른 후 로그인 후 토큰이 순환되기 땜누에 양식이 있는 페이지를 다시 로드해야 할 수 있습니다.

```
Django 설정 파일에 DEBUG=TRUE 가 있기 때문에 이 페이지의 도움말 섹션이 표시됩니다. 
FALSE로 변경하면 초기 오류 메시지만 표시됩니다. 
CSRF_FAILURE_VIEW 설정을 사용하여 이 페이지를 사용자 정의 할 수 있습니다. 
```



#### 1-2.  {% csrf_token %} 

> * ##### {% csrf_token %} 추가하여 다시 확인해본 결과 다음과 같은 오류 메시지를 확인 할 수 있다. 

![image](https://user-images.githubusercontent.com/99783474/193913185-29b49074-f15b-4378-8b9f-5fc3baf7b667.png)



> * ##### POST 로 요청하게 되면 꺼내는 방법이 다르다. 

![image](https://user-images.githubusercontent.com/99783474/193913219-b746a30a-b35f-4d57-a50c-94af49f01ade.png)



> * #####  GET 를 POST로 수정해주면 원하는 정보를 GET 할 수 있다. 

![image](https://user-images.githubusercontent.com/99783474/193913273-69cfe082-166c-47f3-8014-7166ad97a665.png)



> * ##### 아주 큰 변화 : HTTP 주소가 바뀌지 않는다. 
>
> * ##### POST 요청은 주소로서 들어가는 것이 아닌, 요청 메세지에 담겨서 전송이 되기 때문이다. 

![image](https://user-images.githubusercontent.com/99783474/193913308-d544ab2c-2ca2-4cf3-bc19-03c075b0f792.png)



#### 1-3. URL 평점

#### [developers.themoviedb](https://developers.themoviedb.org/3/movies/get-movie-reviews)


![image](https://user-images.githubusercontent.com/99783474/193913344-ce21d8bc-fef6-41be-8f5c-b05d1c528e13.png)




> * ##### 만약, URL 평점을 기록하고 싶다면? 
>
>   * ##### POST/movies/123/score
>
>   * ##### 무조건 등록해야 한다.  WHY? `POST` 가 달려 있기 때문이다. 
>
> * ##### 평점 조회 
>
>   * ##### GET/movie/123/score
>
>   * ##### 무조건 조회해야 한다.  WHY? `GET` 이 달려 있기 때문이다. 



---

#### 1-4. 흐름 정리 

##### (1) METHOD를 POST로 정의하기 

```HTML
<form action="{% url 'articles:create' %}" method="POST">
```

##### (2) {% csrf_token %} 반드시 작성하기 

```HTML
<form action="{% url 'articles:create' %}" method="POST">
{% csrf_token %} 
```

##### (3) 값을 받을 때 POST request로 작성하기 

```python
def create(request):
    # 실제 DB에 저장하는 로직
    title = request.POST.get("title")
    content = request.POST.get("content")
    Article.objects.create(title=title, content=content)
    return redirect("articles:index")
```

---



### <span style='background-color:#fff5b1'>   🐤 Django ModelForm </span>



##### 1. input 태그에 required 추가 

![image](https://user-images.githubusercontent.com/99783474/193913422-6c3fb9f1-0923-4d59-80e8-7c69238c04d1.png)



##### 2.  forms.py

> * ##### artice_form.as_P

![image](https://user-images.githubusercontent.com/99783474/193913451-4ea7ea8f-5602-4508-ba28-6914bdcaf9f3.png)


![image](https://user-images.githubusercontent.com/99783474/193913483-5fd068c4-c55d-4111-8241-ff6d20a8adec.png)


> ##### P 태그로 감싸져 있는 LAVEL, 그리고 INPUT 



##### 3.  유효성 검사 

![image](https://user-images.githubusercontent.com/99783474/193913540-0326202a-be6a-48da-bcd5-236a4ae74f32.png)

![image](https://user-images.githubusercontent.com/99783474/193913568-14200183-b29f-439d-ac45-1fc3a1cea2ad.png)



> ##### 구글 로그인 처럼 form 에 추가한 코드와 결과물은 다음과 같다. 

![image](https://user-images.githubusercontent.com/99783474/193913601-4fc35945-d491-48b8-a737-18a95c591260.png)



##### 4. 코드 합치기  

##### (1) new를 없애고, create 같은 url 에서 처리한다. 

##### (2) 만약, request.method == 'POST' 라면 DB에 저장을 한다. 

##### (3) 그게 아니라면, ariticle_form = ArticleForm()

##### (4) 코드를 하나로 합쳤다면, index.html {% url 'articles:create' %} 라고 변경해준다. 

##### (5) url 에서도 path new 를 없애준다. 

![image](https://user-images.githubusercontent.com/99783474/193913643-e6173a4f-df5f-432c-bee8-065f7763910c.png)

##### 5.  코드 수행 구간 

##### (1) create 실행했을 때

##### (2) 글쓰기 버튼을 눌렀을 때 

![image](https://user-images.githubusercontent.com/99783474/193913678-e045998b-7b89-4099-b1bc-1e21a0d4dbf5.png)

##### (3) invalid 

![image](https://user-images.githubusercontent.com/99783474/193913708-36f80b49-6c0f-4374-84ed-40b4b6e2d454.png)



---



### <span style='background-color:#fff5b1'>   🐤 상세 보기   </span>

> ##### 특정한 글을 본다. 

> ##### http://localhost:8000/articles/create/ 

> ##### ⭐ 반드시 id 값이 들어가야한다. http://localhost:8000/articles/<int:pk>/

#### ⭐ 특정한 글을 본다? 즉, DB에 있는 아이디 값을 URL에 넣어줘야한다. 



##### 1. URL 

![image-20221005033257734](../imges/Django CRUD/image-20221005033257734.png)

##### 2. VIEW

![image-20221005033551665](../imges/Django CRUD/image-20221005033551665.png)



##### 3. detail.html

![image-20221005033818103](../imges/Django CRUD/image-20221005033818103.png)



##### 4. URL (index.html)

![image-20221005034033925](../imges/Django CRUD/image-20221005034033925.png)



##### 5. 결과물 확인 

![image-20221005034155001](../imges/Django CRUD/image-20221005034155001.png)



---



### <span style='background-color:#fff5b1'>   🐤 삭제하기 </span>

> #####  . http://localhost:8000/articles/<int:pk>/delete/

> ##### 특정한 글을 삭제한다. 

---



### <span style='background-color:#fff5b1'>   🐤 수정하기 </span>

> ##### 특정한 글을 수정한다 라는 건 사용자에게 수정된 글을 받아서 특정한 글을 수정한다. 

> ##### 사용자에게 수정할 수 있는 양식을 제공하고 (GET), 특정한 글을 수정한다. (POST)

> #####  http://localhost:8000/articles/<int:pk>/update/



#### ✔ 사용자에게 수정할 수 있는 양식을 제공하고 (GET)



##### 1. URL

![image-20221005034821847](../imges/Django CRUD/image-20221005034821847.png)



##### 2.  수정하기 버튼 생성 (detail.index)

> articles 오타 

![image-20221005035034049](../imges/Django CRUD/image-20221005035034049.png)



##### 3. view

![image-20221005035623893](../imges/Django CRUD/image-20221005035623893.png)

##### 4. update.html

#### ⭐ form 에서 중요한 2가지 요소 

##### ⭐ input : name, value

##### ⭐ action : method (어떤 방식으로)

![image-20221005040213494](../imges/Django CRUD/image-20221005040213494.png)

##### 5. 글을 수정하기 위해 원래 있던 글이 남아있게 하려면? 

![image-20221005040516317](../imges/Django CRUD/image-20221005040516317.png)

##### 6. Forbidden 오류 발생 

![image-20221005040655232](../imges/Django CRUD/image-20221005040655232.png)

![image-20221005040805122](../imges/Django CRUD/image-20221005040805122.png)

> ##### csrf token  작성하기 



#### ✔ 특정한 글을 수정한다. (POST)



##### 1. POST : input 값 가져와서, 검증하고, DB 에 저장

![image-20221005041940387](../imges/Django CRUD/image-20221005041940387.png)

##### 2.  update VS create

![image-20221005042045306](../imges/Django CRUD/image-20221005042045306.png)



---



### 최종 정리 

![image-20221005042820956](../imges/Django CRUD/image-20221005042820956.png)

![image-20221005043101761](../imges/Django CRUD/image-20221005043101761.png)

#### 1. GET 요청일 때 처리 흐름

#### 2. POST 요청일 때 처리 흐름

#### 3. VALID 할 때 

#### 4. INVALID 할때 
