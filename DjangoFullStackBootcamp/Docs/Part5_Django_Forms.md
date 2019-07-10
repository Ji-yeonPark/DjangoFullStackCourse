# Django Forms

> django `Forms`는 <br/>
> HTML Form 위젯을 빠르게 만들어주고, Django Models와 연결해준다.<br/>

- Django Forms의 이점
 - HTML Form 위젯을 빠르게(쉽게) 만들 수 있다.
 - 데이터를 검증하여 Python 데이터 구조로 처리한다.
 - Models 로부터 생성되며, 빠르게 Models 를 업데이트할 수 있다.

- 앱(application) 안에 `forms.py`을 통해 생성 가능하다.
- Django에 이미 설치되어 있는 forms 클래스를 이용해서 불러와서 사용 가능하다.
- models생성하는 것과 매우 비슷하다.


### 1. 설정 방법 (1)

1. `forms.py` 파일을 앱 폴더 내에 생성
```python
# forms.py
# example 
from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
```
2. `views.py`에서 forms를 추가.
```python
# views.py
from . import forms
from forms import FormName

def form_name_view(request):
    form = forms.FormName()
    return render(request, 'form_name.html', {'form': form})
```

3. 보낸 form 을 `html`에 표시한다.
```html
<!-- form_name.html  -->
{{ form }}
```

예)
```html
<div class="container">
    <form method="POST">
        {{ form.as_p }}
        {% csrf_token %}
        <input type="submit" class="btn btn-primary" value="Submit">
    </form>
</div>
```

4. `Views.py`에서 form에서 전달받은 값 접근.

`cleaned_data`로 접근 가능하다.
```python
# views.py
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print ("Form validation Success.")
            print ("Name : " + form.cleaned_data['name'])
            print ("email : " + form.cleaned_data['email'])
            print ("text : " + form.cleaned_data['text'])
    return render(request,  'form_page.html', {'form': form})
```

5. Validator 생성.

- 방법1. custom validator생성
```python
# forms.py

# custom validation
def check_for_z(value):
    # 이름의 첫글자가 z가 아닌 경우 오류 발생
    if value[0].lower() != 'z': raise forms.ValidationError("name needs to start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
```

- 방법2. django.core의 validators이용
```python
# forms.py

from django.core import validators
class FormName(forms.Form):
    botcatcher = forms.CharField(
        required=False, 
        widget=forms.HiddenInput, 
        validators=[validators.MaxLengthValidator(0)])
```

- 방법3. clean 함수에서 체크
```python
# forms.py

class FormName(forms.Form): 
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    text = forms.CharField(widget=forms.Textarea)
    
    # 특정 필드 form 제거 : clean_필드명 
    def clean_botcatcher(self):
            botcatcher = self.cleaned_data['botcatcher']
            if len(botcatcher) > 0:
                raise forms.ValidationError('GOTCHA BOT!')
            return botcatcher

    # 전체 form 제거
    def clean(self):
        all_clean_data = super(FormName, self).clean() 

        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")
```

### 1. 설정 방법 (2) : Model Forms이용

1. `models.py`에 테이블 선언
```python
# models.py
from django.db import models

# Create your models here
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
```


2. `forms.py`에서 선언한 model 정보 불러옴<br/>
`forms.ModelForm`가 포인트!
```python
# forms.py

from first_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
```


3. `views.py`에서 forms를 이용하여 데이터베이스에 데이터 삽입 및 validation 체크 가능
```python
# views.py
from django.shortcuts import render
from .forms import NewUserForm

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():  # Check the validation
            form.save(commit=True)
            return index(request)
        else:
            print ('ERROR FROM INVALID')

    return render(request, 'first_app/users.html', {'form': form})
```

