# Django CRUD 

![image-20221004141546130](../imges/Django CRUD/image-20221004141546130.png)

![image-20221004141641616](../imges/Django CRUD/image-20221004141641616.png)



---



### <span style='background-color:#fff5b1'>   🐣 CRUD   </span>



##### 1) 가상환경 설치하기 

> ##### 가상환경 설치를 왜 하는 걸까?  => 패키지를 별도로 가져가기 위해 설치한다. 

```bash
$ python -m venv venv
```

![image-20221004144830298](../imges/Django CRUD/image-20221004144830298.png)

* ##### ativate  실행이 핵심 

```bash
$ source venv/Scripts/activate 
(venv)
```



##### 2) Django 설치 

```bash
$ pip install django==3.2.13
```

![image-20221004145343621](../imges/Django CRUD/image-20221004145343621.png)



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
> ![image-20221004145755239](../imges/Django CRUD/image-20221004145755239.png)



##### 4) 프로젝트 생성

```bash
$  django-admin startproject pjt . 
```

![image-20221004151933282](../imges/Django CRUD/image-20221004151933282.png)

```bash
$ python manage.py runserver
```

![image-20221004152121134](../imges/Django CRUD/image-20221004152121134.png)

> * #####  settings.py 에서 다음과 같이 내용 수정하기 : 한글 버전
>
> ![image-20221004152347648](../imges/Django CRUD/image-20221004152347648.png)
>
> ![image-20221004152406911](../imges/Django CRUD/image-20221004152406911.png)
>
> * ##### 서버 로그 확인하기 
>
> ![image-20221004152707421](../imges/Django CRUD/image-20221004152707421.png)



##### 5) **Articles** app **생성**

```bash
$ python manage.py startapp articles
```

![image-20221004153415436](../imges/Django CRUD/image-20221004153415436.png)

![image-20221004153754230](../imges/Django CRUD/image-20221004153754230.png)

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

![image-20221004154256124](../imges/Django CRUD/image-20221004154256124.png)

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

![image-20221004160508181](../imges/Django CRUD/image-20221004160508181.png)



##### 6) articles > urls.py 생성

```python
URL 설정을 app 단위로 했들 때 반드시 들어가야 하는 것
=> urlpatterns
```

![image-20221004161319547](../imges/Django CRUD/image-20221004161319547.png)

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

![image-20221004162208064](../imges/Django CRUD/image-20221004162208064.png)

---



![image-20221004162543002](../imges/Django CRUD/image-20221004162543002.png)



> ##### 1. ' ___ ' 라는 경로로 들어가면,  views.index 라는 함수를 실행할 것이다. 그리고 그것을 index라는 이름으로 부를 것이다. 
>
> * ##### NameError : name 'views' is not defined
>
> ##### 2. from . import views
>
> * ##### AttributeError : module 'articles.views' has no attribute 'index'



##### 6) articles > views.py 함수 정의 

* ##### views 파일 구성 

![image-20221004164123258](../imges/Django CRUD/image-20221004164123258.png)

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "articles/index.html")
```



##### 7) Template 생성

![image-20221004164500057](../imges/Django CRUD/image-20221004164500057.png)

> ##### index.html

![image-20221004165054080](../imges/Django CRUD/image-20221004165054080.png)



---

* #### 다시 흐름잡기 

![image-20221004170150992](../imges/Django CRUD/image-20221004170150992.png)

![image-20221004170336033](../imges/Django CRUD/image-20221004170336033.png)

---



### <span style='background-color:#fff5b1'>   🐤 CRUD   </span>



#### 1. 모델(모형) 정의하기 (DB 스키마 설계)

---

![image-20221004173956589](../imges/Django CRUD/image-20221004173956589.png)

---

> ##### 어떤 모형? 시스템 기반의 모형 

> ##### UI(기능) 에 따라서 DB가 결정된다. 즉, UI와 DB는 밀접한 관계를 가질 수 밖에 없다. 

![image-20221004173325218](../imges/Django CRUD/image-20221004173325218.png)

![image-20221004173308218](../imges/Django CRUD/image-20221004173308218.png)

---



##### (1) 클래스 정의 

![image-20221004174125273](../imges/Django CRUD/image-20221004174125273.png)



##### (2) 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations
```

![image-20221004174154299](../imges/Django CRUD/image-20221004174154299.png)



##### (3) DB 반영

```BASH
$ python manage.py migrate
```

![image-20221004174349138](../imges/Django CRUD/image-20221004174349138.png)



##### (4) DB 반영 확인하기 

```bash
$ python manage.py showmigrations
```

![image-20221004174902490](../imges/Django CRUD/image-20221004174902490.png)





### <span style='background-color:#fff5b1'>    🐥 CRUD 기능 구현 _ 01. 생성      </span>



### 1. 게시글 생성 

---

#### ⭐ 내가 어떠한 기능을 만들고 싶다면,

#### <span style='background-color: #ffdce0'>URL 에 mapping 되는 VIEW 함수는  각각 1개가 필요하다. </span>

#### 	🤔 WHY?  특정 URL의 각각 기능들이 다르기 때문이다. 

---

![image-20221004180309872](../imges/Django CRUD/image-20221004180309872.png)

---

![image-20221004181330051](../imges/Django CRUD/image-20221004181330051.png)

> ##### 자연스럽게 게시글 생성이라는 것을 만들고 싶다면 첫번째 사용자에게 HTML 을 주는 기능과 두번째 DB에 저장하는 기능을 생각해 볼 수 있다. 따라서 2개의 URL과 2개의 VIEW 함수가 만들어진다. 
>
> ##### ⭐ 동일한 URL에서 처리할 수 없다는 점 반드시 기억하기 



#### 1-1. HTML Form 제공

> ##### http://localhost:8000/articles/new 이미 설계가 된 상태에서 작성을 하는 것!

> ##### 사용자가 INPUT를 사용할 수 있도록 완성 



##### (1) URL 

![image-20221004181726580](../imges/Django CRUD/image-20221004181726580.png)

##### (2) view

![image-20221004181900225](../imges/Django CRUD/image-20221004181900225.png)

##### (3) new.html 파일 생성

![image-20221004190929102](../imges/Django CRUD/image-20221004190929102.png)

![image-20221004190856139](../imges/Django CRUD/image-20221004190856139.png)



사용자가 INPUT를 사용할 수 있도록 완성 

#### ![image-20221004193229417](../imges/Django CRUD/image-20221004193229417.png)

#### 1-2. 입력받은 데이터 처리 

> ##### http://localhost:8000/articles/create/ 

> ##### 사용자로부터 값을 받아서 처리하도록 완성 

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

##### (3) Articles 라는 클래스는 models.py에 있는 모델이다. 

![image-20221004224131054](../imges/Django CRUD/image-20221004224131054.png)



##### (4) 게시글 DB에 생성 후 INDEX 페이지로 redirect

> ##### redirect import 하기 

![image-20221004224318033](../imges/Django CRUD/image-20221004224318033.png)



> ##### 다시 index 로 돌아가줘 
>
> ```python
> return redirect('articles:index')
> ```

![image-20221004224432346](../imges/Django CRUD/image-20221004224432346.png)



##### (5) 작성 버튼 생성

![image-20221004225656648](../imges/Django CRUD/image-20221004225656648.png)

![image-20221004225728562](../imges/Django CRUD/image-20221004225728562.png)

![2022-10-04 22;58;26](../imges/Django CRUD/2022-10-04 22;58;26.gif)

---



### 2. 게시글 목록 기능 구현 



#### 2-1. HTML Form 제공

#### ⭐ DB에서 게시글을 가져와서, template에 전달 

![image-20221004230355150](../imges/Django CRUD/image-20221004230355150.png)

![image-20221004230556892](../imges/Django CRUD/image-20221004230556892.png)



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

![image-20221004231102664](../imges/Django CRUD/image-20221004231102664.png)

---

![image-20221004231859947](../imges/Django CRUD/image-20221004231859947.png)

---



#### 2-3. http://localhost:8000/articles/

![image-20221004232013259](../imges/Django CRUD/image-20221004232013259.png)



> ##### 🤔 만약 제일 나중에 작성했던 글이 게시판 목록 위로 가져오고 싶다면?  다음과 같이 코드를 작성한다. 

![image-20221004232335293](../imges/Django CRUD/image-20221004232335293.png)

![image-20221004232407674](../imges/Django CRUD/image-20221004232407674.png)



---

#### 2-3. 흐름 정리 _ 변수 이름 주의

##### (1) DB 에서 값을 가지고 온다. 

##### (2) Template에 context 로 전달한다. 

##### (3) aricles(index.html)의 name 영향은 context 딕셔너리 key값이다. 

##### (4) `Article.objects.order_by('-pk')` 은 쿼리셋 (Article 객체를 가진) 이다. 

![image-20221004233335179](../imges/Django CRUD/image-20221004233335179.png)

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

![image-20221005013159116](../imges/Django CRUD/image-20221005013159116.png)

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

![image-20221005014900119](../imges/Django CRUD/image-20221005014900119.png)



> * ##### POST 로 요청하게 되면 꺼내는 방법이 다르다. 

![image-20221005015051589](../imges/Django CRUD/image-20221005015051589.png)



> * #####  GET 를 POST로 수정해주면 원하는 정보를 GET 할 수 있다. 

![image-20221005015256012](../imges/Django CRUD/image-20221005015256012.png)



> * ##### 아주 큰 변화 : HTTP 주소가 바뀌지 않는다. 
>
> * ##### POST 요청은 주소로서 들어가는 것이 아닌, 요청 메세지에 담겨서 전송이 되기 때문이다. 

![image-20221005015421934](../imges/Django CRUD/image-20221005015421934.png)

![image-20221005015547840](../imges/Django CRUD/image-20221005015547840.png)



#### 1-3. URL 평점

#### [developers.themoviedb](https://developers.themoviedb.org/3/movies/get-movie-reviews)

![image-20221005015943665](../imges/Django CRUD/image-20221005015943665.png)

##### 저장하고 기록하는 행위(로그인) => POST

![image-20221005020028456](../imges/Django CRUD/image-20221005020028456.png)

##### 조회 하는 행위(검색하는 창) => GET



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

![image-20221005021723575](../imges/Django CRUD/image-20221005021723575.png)



##### 2.  forms.py

> * ##### artice_form.as_P

![image-20221005023159697](../imges/Django CRUD/image-20221005023159697.png)

##### ![image-20221005024252371](../imges/Django CRUD/image-20221005024252371.png)



> ##### P 태그로 감싸져 있는 LAVEL, 그리고 INPUT 



##### 3.  유효성 검사 

![image-20221005025746084](../imges/Django CRUD/image-20221005025746084.png)

![image-20221005025757951](../imges/Django CRUD/image-20221005025757951.png)



> ##### 구글 로그인 처럼 form 에 추가한 코드와 결과물은 다음과 같다. 

![image-20221005030216806](../imges/Django CRUD/image-20221005030216806.png)



##### 4. 코드 합치기  

##### (1) new를 없애고, create 같은 url 에서 처리한다. 

##### (2) 만약, request.method == 'POST' 라면 DB에 저장을 한다. 

##### (3) 그게 아니라면, ariticle_form = ArticleForm()

##### (4) 코드를 하나로 합쳤다면, index.html {% url 'articles:create' %} 라고 변경해준다. 

##### (5) url 에서도 path new 를 없애준다. 

![image-20221005031537650](../imges/Django CRUD/image-20221005031537650.png)

##### 5.  코드 수행 구간 

##### (1) create 실행했을 때

##### (2) 글쓰기 버튼을 눌렀을 때 

![image-20221005032304464](../imges/Django CRUD/image-20221005032304464.png)

##### (3) invalid 

![image-20221005032242448](../imges/Django CRUD/image-20221005032242448.png)



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