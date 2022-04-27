# pjt00

** commit 찍기

** CustomUser 



## 0423

### 0. 환경세팅

- startproject
- startapp - feeds, accounts



## 0427

### 1. Model

- User(Abstract)
  - email
  - phonenumber
  - name
    - fist_name, last_name 구분 안한다.
  - username(unique=True)
  - password

- feed
  - user
  - like_users
  - image
  - content
  - created_at
- comment (cf) reply
  - feed
  - user
  - content
  - created_at
  - like_users



나랑 관계있는 사람만 피드 보여줄 것. index없어도 될 듯

