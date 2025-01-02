# On-boarding > Mini Project
## About
본 프로젝트는 On-boarding 과정에서 진행한 사용자별로 계정 정보 조회 및 컨테이너를 생성할 수 있도록 구현한 API 입니다. </br>
- 사용자는 해당 API에서 회원가입 및 로그인을 통해 사용자 정보를 조회할 수 있습니다.
- 사용자마다 독립적인 환경에서 머신러닝/딥러닝 연구가 가능한 컨테이너를 생성할 수 있습니다. 컨테이너는 사용자의 `username`으로 생성되며, 사용자당 1개씩 생성할 수 있습니다.

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
`$ git clone https://github.com/horang0210/Jay_miniproject.git`</br>
`$ cd Jay`</br>
`$ python manage.py makemigrations` </br>
`$ python manage.py migrate` </br>
`$ python manage.py runserver` &rarr; django server를 브라우저로 확인</br>

---
## Execution
### Run virtual environment & server
`$ source [venv 이름]/bin/activate`  (windows에서 실행 시 `[venv 이름]\Scripts\activate`)</br>
`$ cd Jay`</br>
`$ python manage.py runserver` &rarr; django server를 브라우저로 확인</br>

&darr; 아래의 링크에서 api 명세를 확인 후 DRF에서 제공하는 browsable api에서 진행</br>
[API 명세서](https://www.notion.so/API-1661370fcdd54fc7987f7e48e42192c8?pvs=4)