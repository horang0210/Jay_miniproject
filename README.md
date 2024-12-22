# On-boarding > Mini Project3
## About
- Django, Django Rest Framework를 이용한 Login, 회원가입 API 구현
- Function
  - ID, Password, 이름, 전화번호를 입력하는 회원가입 API
  - ID, Password를 이용한 로그인 API & 로그아웃 API
  - 사용자의 정보를 조회하는 API
    - 사용자 정보 조회는 로그인한 사용자만 사용할 수 있음
    - 사용자는 본인 정보만 조회할 수 있음

---
## Installation
### Install Python
`$ pip install python>=3.10`</br>
&rarr; python version은 3.10 이상이어야 django 5.x 버전을 지원함 </br>

### Virtual Environment 
`$ python -m venv [venv 이름] `</br>
`$ source [venv 이름]/bin/activate`  (windows에서 실행 시 `[venv 이름]\Scripts\activate`)</br>
&rarr; 가상환경을 나가려면 `$ deactivate` </br>
&rarr; 가상환경을 삭제하고 싶다면 `$ rm -rf [venv 이름]` (windows에서 실행 시 `rmdir /s /q [venv 이름]`)</br>

### Django & Django Rest Framework
`$ pip install django==5.1`</br>
`$ pip install djangorestframework==3.15`</br>
&rarr; 설치된 패키지 확인이 필요하다면 `$ pip freeze `</br>

### Get server code & Run server
`$ git clone https://github.com/horang0210/Jay_miniproject_03`</br>
`$ cd Jay`</br>
`$ python manage.py runserver` &rarr; 8000번 포트로 올라간 server 확인</br>

---
## Execution
### Get server code & Run server
`$ source [venv 이름]/bin/activate`  (windows에서 실행 시 `[venv 이름]\Scripts\activate`)</br>
`$ cd Jay`</br>
`$ python manage.py runserver` &rarr; 8000번 포트로 올라간 server 확인</br>
