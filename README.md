# 코드어스 웹앱커밋 프로젝트 2팀

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
.
├── LICENSE
├── docker-compose.yml
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── flask
│   ├── modules
│   │   └── DBHandler
│   │   ├── handler.py
│   │   └── **init**.py
│   ├── db
│   │   └── avengers.sqlite
│   ├── models
│   │   ├── avengers.py
│   │   └── **init**.py
│   ├── Dockerfile
│   ├── uwsgi.ini
│   ├── run.py
│   ├── requirements.txt
│   ├── util
│   │   └── apikey_gen.py
│   ├── static
│   │   ├── caution.png
│   │   └── styles.css
│   ├── main.py
│   └── templates
│   └── index.html
├── README.md
└── structure.txt

9 directories, 20 files
```
