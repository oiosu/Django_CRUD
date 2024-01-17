### 11_Django_session

```python
MIDDLEWARE =[
    "django.contrib.sessions.middleware.SessionMiddleware"
]
```



* ##### Django session 종류 

> SESSION_ENGINE
>
> `django.contrib.sessions.backends.db`
>
> `django.contrib.sessions.backends.file`
>
> `django.contrib.sessions.backends.cache`
>
> `django.contrib.sessions.backends.cache_db`
>
> `django.contrib.sessions.backends.signed_cookes`



* ##### JWT와 다른 점

|                 | JWT            | Django session      |
| --------------- | -------------- | ------------------- |
| 요청마다 DB조회 | Optional       | Must                |
| 정보 변경       | 가능           | 가능                |
| 저장 방식       | 모든 방법 가능 | 쿠키                |
| 보안            | 우수           | 매우우수(HTTPS사용) |

