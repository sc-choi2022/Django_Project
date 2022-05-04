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



나랑 관계있는 사람만 피드 보여줄 것. index없어도 될 듯 하다.



## 0504

### . Model

- User(Abstract)
  - email(unique=True)
  - phonenumber(unique=True)
  - username(unique=True)
  - password
  - followings

```python
#accounts/models.py
class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    followings = models.ManyToManyField('self', symmetrical=False, 
    related_name='followers')
```



- feed
  - user
  - like_users
  - image
  - content
  - created_at

```python
#feeds/models.py
class Feed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_feeds')
    # 이미지 업로드 날짜에 따라 디렉토리에 저장 (strftime 으로 포멧팅)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
```



- comment (cf) reply
  - feed
  - user
  - content
  - created_at
  - like_users

```python
#feeds/models.py
class Comment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')

    def __str__(self):
        return self.content
```



signup을 만들기 위해 index 관련 url, views, templates 코드를 작성했다.

 

### error

이미지를 삽입하기 위해 Pillow 설치 및 requirement.txt에 반영했다.

settings.py 오류로 clushed error 발생하여 setting.py 새로 작성했다.

