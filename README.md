# README.md

## 1. 백엔드 컨벤션

1. main branch터치 금지, 새 브랜치를 만들때는 dev를 통해 만들것(특히 feature 브랜치를 만들때)
2. branch naming 규칙
    1. 기능을 추가하기 위한 브랜치 : feature/name(본인 영문이름)/기능명
    2. 기능을 수정(오류 등의 이유로)하는 경우 : hotfix/name(본인 영문이름)/기능명
3. merge를 해야하는 경우에는 pull req만 걸어두고, 팀장에게 카톡등으로 연락할것
4. 가상환경의 이름은 'venv'로 통일 할것
5. 설치해야하는 패키지들은 requirement.txt 참고
   1. pip install -r requirement.txt