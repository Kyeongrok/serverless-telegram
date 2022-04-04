## Pipenv사용

### 패키지 설치
* pipenv install numpy

### sls 전체 배포
* sls deploy --stage dev

### sls 특정 function만 배포
* sls deploy function -f findBetween --stage dev

### 배포 후 test
* sls invoke -f hello --log

### local test
* sls invoke local -f hello --log

### 로그 보기
* sls logs -f hello


