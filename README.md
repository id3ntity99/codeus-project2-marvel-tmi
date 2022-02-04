# 코드어스 웹앱커밋 프로젝트 2팀

## 프로젝트 소개

- 마블 캐릭터들에 관한 잡다한 정보 (특정 캐릭터가 몇번 출연했는지, 몇번 죽었는지 등)를 볼 수 있는 웹 어플리케이션 입니다.

## 사용 스택

(이미지)

- 프레젠테이션 레이어는 React와 Typescript를, 비즈니스 레이어는 Flask, Flask-sqlalchemy를, 퍼시스턴스 레이어는 SqlAlchemy를, 데이터베이스 레이어는 sqlite3를 이용하여 구현하였습니다.(데이터베이스는 추후 MySQL로 변경할 예정입니다.)
- Docker를 통해 컨테이너를 구성하고 AWS EC2를 이용하여 웹 서비스를 배포하였으며 S3 버킷을 이용해 프론트엔드를 배포하였습니다.
- Nginx를 이용하여 Reverse proxy API gateway를 구현하였습니다.

## 아키텍처

- MVC 패턴에 기반한 4티어 레이어드 아키텍처
  (이미지)

## 웹 페이지

(이미지)

## 팀원

| 역할         | 이름   |
| ------------ | ------ |
| 팀장(프론트) | 최수정 |
| 팀원(프론트) | 이재훈 |
| 팀원(백엔드) | 이민서 |
| 팀원(백엔드) | 이현민 |
| 팀원(백엔드) | 배진현 |

## 커밋 메시지 컨벤션

- <타입> : <제목>

- <타입> 리스트:
  |타입|설명|
  |----|----|
  |feat|새로운 기능 추가|
  |fix|버그 수정|
  |refact|리팩토링|
  |docs|문서 추가, 수정, 삭제|
  |test|테스트코드 수정, 추가, 삭제|
  |chore|기타 변경사항|

## 브랜칭 전략

1. 새로운 이슈를 생성하고 이슈 번호를 확인한다.
2. 로컬 저장소에 issue/#이슈번호 형식으로 새로운 브랜치를 생성한다.
3. 이슈에 적어둔 내용을 수행한다.
4. 작업 내용에 대한 테스트를 진행한다.
5. 작업 내용을 커밋하고 원격 저장소로 push한다.
6. 리뷰를 거친 후 작업 브랜치를 main 브랜치에 merge한다.
7. 이슈를 닫고 작업 브랜치도 삭제한다.

## 디렉터리 구조

```
codeus-project2-marvel-tmi
├── back
│   ├── docker-compose.yml
│   ├── flask
│   │   ├── db
│   │   │   ├── avengers.sqlite
│   │   │   └── test.sqlite
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── model.py
│   │   ├── modules
│   │   │   └── DBHandler
│   │   │       ├── handler.py
│   │   │       └── __init__.py
│   │   ├── requirements.txt
│   │   ├── run.py
│   │   ├── static
│   │   │   ├── caution.png
│   │   │   └── styles.css
│   │   ├── templates
│   │   │   └── index.html
│   │   ├── test
│   │   │   └── test_api.py
│   │   ├── util
│   │   │   └── apikey_gen.py
│   │   └── uwsgi.ini
│   └── nginx
│       ├── Dockerfile
│       └── nginx.conf
├── front
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   └── index.html
│   ├── README.md
│   ├── src
│   │   ├── App.tsx
│   │   ├── atom
│   │   │   └── atoms.ts
│   │   ├── components
│   │   │   ├── Avenger
│   │   │   │   ├── index.tsx
│   │   │   │   └── styles.tsx
│   │   │   ├── DarkModeButton
│   │   │   │   ├── index.tsx
│   │   │   │   └── styles.tsx
│   │   │   └── header
│   │   │       ├── index.tsx
│   │   │       └── styles.tsx
│   │   ├── index.tsx
│   │   ├── pages
│   │   │   ├── Home
│   │   │   │   ├── index.tsx
│   │   │   │   └── styles.tsx
│   │   │   └── Search
│   │   │       └── index.tsx
│   │   ├── react-app-env.d.ts
│   │   ├── styles
│   │   │   ├── global-style.ts
│   │   │   ├── styled.d.ts
│   │   │   └── theme.ts
│   │   ├── typings
│   │   │   └── db.ts
│   │   └── utils
│   │       └── api.ts
│   └── tsconfig.json
├── LICENSE
└── README.md

25 directories, 44 files
```
