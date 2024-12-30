# On-boarding > Mini Project
## About
- Django, Django Rest Framework를 이용한 Login, 회원가입 API 구현
- Function
  - ID, Password, 이름, 전화번호를 입력하는 회원가입 API
  - ID, Password를 이용한 로그인 API & 로그아웃 API
  - 사용자의 정보를 조회하는 API
    - 사용자 정보 조회는 로그인한 사용자만 사용할 수 있음
    - 사용자는 본인 정보만 조회할 수 있음

- Django, Django Rest Framework를 이용한 컨테이너 생성 API 구현
- Function
  - 로그인 후 username과 동일한 명칭의 컨테이너를 생성 및 실행할 수 있는 API
    - 컨테이너는 사용자당 1개만 생성 가능함
    - 이미 컨테이너를 생성했을 경우 API 요청을 보내도 새로운 컨테이너를 생성할 수 없음
    - 컨테이너 환경
      - 기본 이미지: ubuntu 20.04
      - CUDA: 11.8
      - cuDNN: 8.6.0
      - NCCL: 2.15.5
      - Anaconda: latest(&rarr; 컨테이너 실행 시 로그인되는 계정의 홈 디렉토리 안에서만 사용 가능) 
      - date: KST

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
`$ python manage.py runserver` &rarr; http://127.0.0.1:8000/ 로 올라간 server 확인</br>

---
## Execution
### Get server code & Run server
`$ source [venv 이름]/bin/activate`  (windows에서 실행 시 `[venv 이름]\Scripts\activate`)</br>
`$ cd Jay`</br>
`$ python manage.py runserver` &rarr; http://127.0.0.1:8000/ 로 올라간 server 확인</br>

### Register & Login
http://127.0.0.1:8000/api/v1/user/register/ 에서 POST로 회원가입 진행</br>
http://127.0.0.1:8000/api/v1/user/login/ 에서 POST로 아래와 같이 선택 및 작성 후 로그인 진행</br>
  - Media type : application/json</br>
  - Content : {"username":"[본인 username]", "password":"[본인 password]"}</br>
http://127.0.0.1:8000/api/v1/user/detail/ 에서 GET으로 사용자 정보 조회 </br>
http://127.0.0.1:8000/api/v1/user/logout/ 에서 GET으로 로그아웃 진행</br>

### Create Container
http://127.0.0.1:8000/api/v1/container/ 에서 GET으로 본인의 컨테이너 정보 조회 </br>
http://127.0.0.1:8000/api/v1/container/ 에서 POST로 본인의 컨테이너 생성</br>
(Content에는 별도의 정보를 작성하지 않음)</br>
※ 이미 컨테이너를 생성한 경우 추가로 컨테이너 생성은 불가함</br>