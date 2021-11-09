# 🎊 Wanted X Wecode PreOnBoarding Backend Course | 무한루프 팀
원티드 2주차 기업 과제 : Wanted Assignment Project
  ✅ 원티드랩 기업 과제입니다.
- [원티드랩 사이트](https://www.wanted.co.kr/newintro?&utm_campaign=brand_sa&utm_source=google&utm_medium=cpc&utm_content=brand&utm_term=%EC%9B%90%ED%8B%B0%EB%93%9C%20%EB%9E%A9&gclid=CjwKCAiA1aiMBhAUEiwACw25MRzvuC5pTgg9QtCSEibJ9HOg-fZSCjiffhkEQXdjgltUXoY8gP3IhhoCcMYQAvD_BwE) 
- [wanted 채용공고 링크](https://www.wanted.co.kr/wd/70371) 

<hr>

# 🔖 목차
- Team 소개
- 과제 내용
- 기술 환경 및 tools
- 모델링 ERD
- API 명세서
- 설치 및 실행 방법


<hr>

# 🧑‍🤝‍🧑 Team 소개

| 이름 | 담당 기능 | 블로그 |
| :---: | :---: | :---: | 
| 공통 | 초기환경 설정, DB 모델링, postman api 문서 작성, README.md 작성, 배포, pytest | X |
| 송치헌 | 회사 이름으로 정보 검색 기능 | |
| 유동헌 | 회사명 자동완성 기능, 더미 데이터 추가 | |
| 하예준 | 회사명 자동완성 기능, 더미 데이터 추가 | |
| 오지윤(팀장) | 회사 추가 기능 | |
| 손희정 | 회사 추가 기능 |  |

<hr>

# 📖 과제 내용
> 다음과 같은 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 REST API 서버를 개발해주세요

### **[필수 포함 사항]**

- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### **[개발 요구 사항]**
- 제공되는 test case를 통과할 수 있도록 개발해야 합니다.    
- ORM 사용해야 합니다.
- 결과는 JSON 형식이어야 합니다.
- database는 RDB를 사용해야 합니다.
- database table 갯수는 제한없습니다.
- 필요한 조건이 있다면 추가하셔도 좋습니다.
- Docker로 개발하면 가산점이 있습니다.

### **[기능 개발]**

✔️ **REST API 기능**

- 회사명 자동완성
    - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가


<hr>

# ➡️ Build(AWS EC2)
API URL : http://3.36.59.83:8000

<br>

# ⚒️ 기술 환경 및 tools
- Back-End: python 3.9.7, Flask-RESTful 0.3.9, PyMySQL
- Deploy: AWS EC2, RDS
- ETC: Git, Github, Postman

<br>

# 📋 모델링 ERD

![wanted_erd](https://user-images.githubusercontent.com/64240637/140931939-781a552f-46ed-46be-a239-85751fd329f1.png)

<hr>

# 🌲 디렉토리 구조
```
├── app.py
├── company
│   ├── controller.py
│   ├── __init__.py
│   ├── models.py
│   └── tests.py
├── config.py
├── CONVENTION.md  
├── PULL_REQUEST_TEMPLATE.md
├── README.md
└── requirements.txt
```
<hr>

# 🔖 API 명세서
[Postman API](https://documenter.getpostman.com/view/14348138/UVC5E7S9)

### 회사 상세 정보

1. 회사 이름을 path parameter로 넣은 뒤 header에 원하는 language를 담아줍니다.
2. 만약 header에 language가 없을 경우 기본값으로 ko에 대한 회사를 보여줍니다.
3. 만약 회사가 존재하지 않는 경우 "Company or Language Not Found"라는 에러 메시지를 반환합니다.

- Method: GET
```
http://3.36.59.83:8000/companies/라인 프레쉬
```

- parameter : path parameter

- response 

```
{
  "company_name": "라인 프레쉬",
  "tags": [
    "태그_1",
    "태그_8",
    "태그_15"
  ]
}
```

### 회사 목록 정보

1. query string으로 들어온 데이터가 포함되는 모든 회사의 정보를 조회합니다.
2. 만약 header에 들어온 language를 지원하지 않는 경우 "COUNTRY_NOT_SUPPORTED"라는 에러 메시지를 반환합니다.
3. 만약 query string으로 들어온 데이터를 포함하고 있는 회사가 없을 경우 "COMPANY NOT FOUND"라는 에러 메시지를 반환합니다.

- Method: GET
```
http://3.36.59.83:8000/search?query=원
```

- parameter : query string

- response
```
[
  {
    "company_name": "원티드"
  },
  {
    "company_name": "원할머니"
  }
]
```

### 회사 생성

1. 회사의 이름과 회사가 지원하는 language, 각 회사가 지원하는 언어의 tag를 body에 입력합니다.
2. header에 들어있는 language로 회사가 생성 되지 않았을 경우 "not found country code"라는 에러 메시지를 반환합니다. 


- Method: POST
```
http://3.36.59.83:8000/companies
```

- parameter : request_body, header parameter(fr입력)

```
{
"company_name": {
    "ko": "직방",
    "fr": "straight",
    "ja": "straight"
},
"tags": [
    {
        "tag_name": {
            "ko": "태그10",
            "fr": "tag10",
            "ja": "tag10"
        }
    },
    {
        "tag_name": {
            "ko": "태그20",
            "fr": "tag20",
            "ja": "tag20"
        }
    },
    {
        "tag_name": {
            "ko": "태그30",
            "fr": "tag30",
            "ja": "tag30"
        }
    }
]
}
```

- response   

```
{
    "company_name": "straight",
    "tags": [
        "tag10",
        "tag20",
        "tag30"
    ]
}
```

# 🔖 설치 및 실행 방법

### 로컬 및 테스트용
1. 해당 프로젝트를 clone하고, 프로젝트로 들어간다.
```
https://github.com/wanted-InfinityLoop/wanted-InfinityLoop.git .
```

2. 가상환경으로 miniconda를 설치한다. [Go](https://docs.conda.io/en/latest/miniconda.html)

```
conda create -n wanted python=3.9
conda actvate wanted
```   

3. 가상환경 생성 후, requirements.txt를 설치한다.

```
pip install -r requirements.txt

Flask-RESTful==0.3.9
Flask-SQLAlchemy==2.5.1
PyMySQL==1.0.2
Flask-Migrate==3.1.0
pytest==6.2.5
```


5. migrate 후 로컬 서버 가동
```
flask db init
flask db migrate
flask db upgrade

python app.py (flask run)
```



