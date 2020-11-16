# Django-Blog



## 기능


### 필수 기능


```
    * 회원 기능
        - authentication
            email

    * 블로그 기능
        - CRUD
        - pagination
    * SEO
        - Sitemap
        - meta
    * Log
        - log text file
```


### 필수 기술


```
    * PEP8
    * 단위 테스트, 통합 테스트
    * Django
    * MySQL
    * Git & Github, Git Flow
    * uWSGI
    * Docker
    * Jenkins CI/CD
```


### 선택 조건


```
    * Setting은 config.py에서 개발, 운용을 구분하여 설정
```


---


## 설정


```
pip install -r requirement.txt
```


#### sqlite3 설정


blog/blog/config/config.py

```
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

KEY_SET = "iHlsPAeadeMeFhv8T9ttE4uwsu3U5b3ava2fKmed4rDj9v9vBN"

DATABASE_SET = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG_SET = True


HOST_SET = ["*"]

CONFIG_EMAIL_USER = "youremail@mail.com"
CONFIG_EMAIL_PASSWORD = "password"
```



#### MySQL 설정

blog/blog/config/config.py

```
import pymysql

pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

KEY_SET = "iHlsPAeadeMeFhv8T9ttE4uwsu3U5b3ava2fKmed4rDj9v9vBN"

DATABASE_SET = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "데이터베이스명",
        "USER": "user id",
        "PASSWORD": "user password",
        "HOST": "데이터베이스 IP",
        "PORT": "데이터베이스 Port",
    }
}

DEBUG_SET = True

# When DEBUG is False and a view raises an exception, all information will be sent by email to the people listed in the ADMINS setting
# ADMINS = (('Admin Name', 'email@gmail.com'),)

HOST_SET = ["*"]

CONFIG_EMAIL_USER = "youremail@mail.com"
CONFIG_EMAIL_PASSWORD = "password"
```
