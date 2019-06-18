# Project Settings Folder

> `first_project`폴더는 아래 명령어를 통해 생성된 **프로젝트 셋팅 폴더**이다.
```bash
$ django-admin startapp [프로젝트이름]

# 예
$ django-admin startapp first_project
```

### 1. 프로젝트 폴더 내 각 파일 설명
1. `__init__.py`

* 빈 파이썬 스크립트 파일. <br/>
(blank Python Script)
* 디렉토리에 이 이름을 갖는 파일이 존재한다면, **이 디렉토리는 패키지**로 다뤄진다는 것을 Python이 알도록 해줌. <br/>

2. `settings.py`

* 프로젝트 셋팅에 대한 정보를 갖는 파일.

3. `url.py`

* 프로젝트의 URL 패턴에 대한 정보를 갖는 파일.
* 기본적으로 웹 어플리케이션의 각 페이지들의 URL들을 선언해둔 곳이라 생각하면 됨.

4. `wsgi.py`

* 웹 서버 게이트웨이 인터페이스(Web Server Gateway Interface) 역할.
* 마지막에 웹 어플리케이션을 서버에 배치할 때 사용됨.

5. `manage.py`

* Django에서 가장 많이 사용되는 스크립트.
* 웹 어플리케이션을 개발하는데 있어서 많은 명령어들(commands)과 연관된다.

```bash
# django web server 실행
# http://127.0.0.1:8000 으로 접속 가능
$ python manage.py runserver
```

## 2. runserver시 발생되는 경고

> You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

그러면 `migrate`와 `migrations`란 무엇인가?<br/>
- Django와 Database를 연결(connect)해주는 방법이다.
- `migrations`을 통해 한 설계(design)에서 다른 설계로 데이터베이스 이동 가능하며, 되돌릴 수도 있음.
- `migrations`를 통해 데이터베이스를 이주(`migrate`)할수 있게 함.
