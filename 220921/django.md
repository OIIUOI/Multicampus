IP와 도메인은 무엇인가

아래 MDN 문서와 외부 자료를 조사해 주어진 질문의 답을 작성하세요.

- 가상환경 생성 / 실행 (터미널에서 명령어)
  
  ```python
  # 가상환경을 설정해줄 폴더 생성
  mkdir test
  # test 폴더 안에 들어가기
  # 파이썬 모듈 중 venv 실행 (test_venv는 가상환경이름)
  python -m venv test_venv
  
  # 가상환경 실행
  source ./script/activate
  ```
- Django LTS 버전 설치
  
  ```python
  pip install django==lts
  
  # testpjt 는 장고에 쓰이는 프로그램 깔리는 폴더
  django-admin startproject testpjt
  ```

- Django 실행
  
  ```python
  python manage.py runserver
  
  
  # localhost 8000 or localhost:8000
  ```
  
  

Q. IP와 도메인은 무엇일까요?

- https://developer.mozilla.org/ko/docs/Learn/Common_questions/How_does_the_Internet_work

| IP                                        | 도메인                              |
| ----------------------------------------- | -------------------------------- |
| 컴퓨터 주소 / '.' 으로 구분된 4개의 숫자 (192.168.2.10) | 컴퓨터 주소를 사람이 읽을 수 있게 (google.com) |

Q. 클라이언트와 서버는 무엇일까요?

- https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/How_the_Web_works
- https://developer.mozilla.org/ko/docs/Learn/Common_questions/What_is_a_web_server(https://developer.mozilla.org/ko/docs/Learn/Common_questions/What_is_a_web_server

| 클라이언트 | 서버   |
| ----- | ---- |
| 요청    | 요청사항 |

Q. 정적 웹 사이트와 동적 웹 사이트의 차이점은 무엇일까요? Django는 무엇을 위한 도구인가요?

- https://developer.mozilla.org/ko/docs/Learn/Server-side/First_steps/Introduction
  
  | 정적 웹 사이트                  | 동적 웹 사이트  |
  | ------------------------- | --------- |
  | 리소스 요청이 들어올 때 동일한 콘텐츠를 반환 | 사용자와 관계되어 |

Q. HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?

- https://developer.mozilla.org/ko/docs/Web/HTTP/Overview



Q. 프레임워크는 무엇일까요?(외부 자료 조사)


