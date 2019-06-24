# Django Application

> django `application`은 전체 웹 애플리케이션을 위해 특정 기능을 수행하도록 생성된다.<br/>
> django app(application)은 다른 django 프로젝트에 연결될 수있다. 즉, **재사용**할 수 있다.
```bash
$ python manage.py startapp [앱 이름]

# 예
$ python manage.py startapp first_app
```

### 1. 앱 폴더 내 각 파일 설명
(part1에서 설명한 파일을 제외하고 정리함.)

1. `admin.py`

* Django admin인터페이스에서 사용할 수 있도록 django model 등록하는 파일. 

2. `apps.py`

* application의 특별한 설정을 할 수 있다.

3. `models.py`

* application의 데이터 모델 저장(정의).

4. `test.py`

* 테스트 함수 저장.

5. `views.py`

* requests를 다루고 response를 받는 함수가 있는 파일.

6. `Migrations` folder

* models 와 연관된 데이터베이스의 상세 정보를 저장하는 디렉토리.


### 2. 프로젝트에 앱 등록 방법

1. 프로젝트 폴더 내 `settings.py`파일 수정<br/>
`INSTALLED_APPS`에 생성한 앱 추가.
```python
INSTALLED_APPS = [
    ...
    'first_app'
]
```

2. url등록<br/>
**방법1.** : 프로젝트 폴더에서 모든 url 관리하는 방법.<br/> 
* 프로젝트 폴더 내 `urls.py`파일 수정<br/>
앱 내의 views파일을 추가한 후 views에 정의한 함수를 정규식을 이용하여 url에 등록시킴.
```python
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

**방법2.** : 각 앱에서 url 관리하는 방법.<br/> 
> `include`를 이용해서 프로젝트 내 urls 파일이 아닌 각 앱안의 urls 파일에 url을 정의할 수 있다.<br/>
> project의 urls파일을 **clean하고 modular하게** 만든다.
* 먼저 프로젝트 내 `urls.py` 파일 수정<br/>
사용하려는 앱을 **include**한다.
```python
from django.conf.urls import include

urlpatterns = [
    url(r'^first_app/', include('first_app.urls'))  # http://도메인/first_app/... 형식이 된다.
]
```
* 앱 폴더안에 urls.py파일을 추가한다.
