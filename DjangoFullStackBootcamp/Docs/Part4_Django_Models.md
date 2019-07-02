# Django Models

> django `Models`는 프로젝트에서 데이터베이스 통합하기위해 사용된다.<br/>
> 기본적으로 SQLite가 장착되어 있지만, 다양한 SQL 엔진을 연결하여 사용이 가능하다.<br/>
> `settings.py` 파일에서 `DATABASE` 파라메터를 갖고 DARABASE 엔진을 수정할 수 있으며,<br/>
> 앱의 `models.py`파일에서 클래스 구조로 실제 모델을 생성할 수 있다.<br/>
> 모델을 만들고 어드민에 등록할 경우, 어드민 페이지에서 쉽게 관리 가능하다.



### 1. 설정 방법

1. settings.py 에서 데이터베이스 셋팅

2. models.py 에서 테이블 정보 클래스 생성

3. 전체 프로세스 적용 <br/>
django session, user, group 등 정보 관련 테이블 자동 생성된다.
```shell
$ python manage.py migrate
```
<img width="472" alt="스크린샷 2019-07-02 오전 12 16 45" src="https://user-images.githubusercontent.com/40231980/60447803-2e0de700-9c5f-11e9-994a-8d768c1d2c13.png">


4. 변경 정보를 등록한다.
```shell
$ python manage.py makemigrations
또는 특정 앱만 등록할 경우
$ python manage.py makemigrations 앱이름
```
<img width="529" alt="스크린샷 2019-07-02 오전 12 18 43" src="https://user-images.githubusercontent.com/40231980/60447802-2e0de700-9c5f-11e9-8550-a0347c71beed.png">

5. 다시 한번더 프로세스에 적용
```shell
$ python manage.py migrate
```
<img width="497" alt="스크린샷 2019-07-02 오전 12 19 15" src="https://user-images.githubusercontent.com/40231980/60447800-2d755080-9c5f-11e9-806c-b65760c6ac83.png">


6. 어드민에 등록 원할 경우 admin.py파일에 코드 추가
```python
# admin.py
from django.contrib import admin
from 앱이름.models import 모델명1, 모델명2

admin.site.register(모델명1)
admin.site.register(모델명2)
```

7. 어드민페이지 접근을 위해 superuser생성
```shell
$ python manage.py createsuperuser
Username (leave blank to use 'jiyeon'): admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.
```


### MTV

> **MTV** 방식이란<br/>
> M : Models : 테이블 정의<br/>
> T : Templates : 클라이언트 화면 정의<br/>
> V : Views : 앱 로직 정의<br/>
> 세 부분으로 나누어 개발하는 방식이다.

- 장점 :<br/>
  - M, T, V간 독립성 유지 가능
  - 데이터베이스관리자(M), 개발자(V), 디자이너(T)간 협업 쉬움.


