# 1. REST
## REST(REpresentational State Transfer)
웹에 존재하는 모든 자원(이미지, 동영상, DB 자원)에 고유한 URI를 부여해 활용하는 것

## URI(Uniform Resource Identifier)
인터넷에 있는 자원을 나타내는 주소

## CRUD(Create Read Update Delete)
자원을 '생성, 조회, 수정, 삭제'하는 작업

----------------------------------------------------

# 2. REST API
## API(Application Programming Interface)
소프트웨어가 다른 소프트웨어로부터 지정된 형식으로 요청, 명령을 받을 수 있는 수단

## REST API
REST를 기반으로 서비스 API를 구현한 것
ex. 프론트엔드 웹에서 서버에 데이터를 요청하거나, 배달 앱에서 서버에 주문을 넣거나 등과 같은 서비스들에서 오늘날 널리 사용되는 것이 REST란 형식의 API이다.

## HTTP(Hyper Text Transfer Protocol)
서버에 REST API로 요청을 보낼 때는 'HTTP'라는 규약에 따라 신호를 전송

## REST API에서 주로 사용하는 'HTTP로 요청을 보낼 때 사용하는 메소드 5가지'
GET, POST, PUT, DELETE, PATCH
(이외에도 더 다양한 메소드가 있음)

## 'GET, POST, PUT, DELETE, PATCH'의 특징
'POST, PUT, PATCH'는 body라는 주머니가 있어서 'GET, DELETE'보다 더 많은 데이터를 비교적 안전하게 감춰서 실어보낼 수 있다.
그런데 이 메소드들이 특정 용도에 제한되어 사용되지는 않는다.
예를 들면 'POST' 하나만으로도 데이터를 생성하고, 조회하고, 수정하고, 삭제하는 기능까지 할 수 있다. 
하지만 누구든 각 요청의 의도를 쉽게 파악할 수 있도록 RESTful하게 API를 만들기 위해서는 각 메소드의 목적에 따라 구분해서 사용해야 한다.

## GET
데이터를 Read, 조회하는데 사용

## POST
데이터를 Create, 새로운 정보를 추가하는데 사용

## PUT
정보를 통째로 갈아끼울 때 사용

## PATCH
정보 중 일부를 특정 방식으로 변경할 때 사용

## DELETE
정보를 삭제할 때 사용

이를 바탕으로 REST API란 HTTP 요청을 보낼 때 어떤 URI에 어떤 메소드를 사용할지 개발자들 사이에 널리 지켜지는 약속을 의미한다는 것을 알 수 있다.

----------------------------------------------------

# 3. RESTful
RESTful이란 REST를 REST 답게 쓰기 위한 방법을 의미한다.
즉, 누구든지 이해하기 쉽고 사용하기 쉬운 REST API를 만드는 것을 의미한다.

## RESTful하지 못한 경우
ex. CRUD 기능을 모두 POST로만 처리하는 API

http://(도메인)/classes/2/students/create
http://(도메인)/classes/2/students/read
http://(도메인)/classes/2/students/update
http://(도메인)/classes/2/students/delete

모두 POST로만 처리하는 API의 경우 '타인이 알아보기 쉽게 하기 위해서'는 위와 같이 URI에 동작까지 명시해야 하는 불편함이 있다.