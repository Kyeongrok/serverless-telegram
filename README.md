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


### 데이터 넘기기
* sls invoke -f call-telegram --log -d '{"a":"bar"}'

### 로그 보기
* sls logs -f hello


## API
### Endpoint
GET - https://jevf3cn1za.execute-api.ap-northeast-2.amazonaws.com/users/create

