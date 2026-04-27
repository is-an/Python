# Python Study Repository

이 저장소는 AWS, Shell, Docker 운용에 도움이 되는 Python 예제들을 난이도별로 정리한 학습용 자료입니다.

## 구성

- `aws/`
  - AWS 관련 Python 예제 5개
  - `boto3`를 사용한 S3, EC2, DynamoDB, Lambda 관련 실습 코드
  - `level1.py`부터 `level5.py`까지 난이도 순서로 구성
  - `test.txt`는 AWS S3 업로드 실습에 사용할 수 있는 예제 파일입니다
- `shell/`
  - Shell 명령을 Python으로 실행하는 예제 5개
  - `subprocess`를 중심으로 명령 실행, 결과 처리, 시스템 정보 조회 학습
- `docker/`
  - Docker 운용 예제 5개
  - `docker-py`를 사용해 이미지 가져오기, 컨테이너 실행, 로그 확인, 볼륨 마운트 등을 실습

## 예제 스타일

각 예제 파일은 다음과 같은 형식으로 구성되어 있습니다.

1. 실행 예제 코드
2. 코드 설명(풀이)
3. 응용 문제

예를 들어 `aws/level1.py`는 S3 버킷 목록 조회 예제이며, `shell/level1.py`는 `ls` 명령을 Python에서 실행하는 예제입니다.

## 실행 방법

터미널에서 해당 폴더로 이동한 뒤 Python으로 실행합니다.

```bash
cd /mygit/Python/aws
python3 level1.py
```

필요한 패키지 설치:

```bash
pip3 install boto3
pip3 install docker
```

## 권장 Python 버전

이 저장소의 AWS 예제는 `boto3`를 사용하므로 Python 3.7 이상을 권장합니다.

## 참고

- AWS 예제는 AWS 자격증명(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY 또는 AWS CLI 설정)이 필요합니다.
- Docker 예제는 로컬 Docker 데몬이 실행 중이어야 합니다.
- Shell 예제는 Linux 환경에서 실행하는 것을 기준으로 작성되었습니다.

## 폴더별 요약

### `aws/`
- `level1.py`: S3 버킷 목록 출력
- `level2.py`: S3 파일 업로드 예제
- `level3.py`: EC2 인스턴스 정보 조회
- `level4.py`: DynamoDB 테이블 생성
- `level5.py`: Lambda 함수 생성 예시

### `shell/`
- `level1.py`: `ls` 명령 실행
- `level2.py`: `pwd` 명령 실행
- `level3.py`: `df -h`로 디스크 사용량 조회
- `level4.py`: `/etc/passwd` 사용자 계정 목록 추출
- `level5.py`: 특정 프로세스 실행 여부 확인

### `docker/`
- `level1.py`: Docker 컨테이너 목록 조회
- `level2.py`: nginx 이미지 pull
- `level3.py`: nginx 컨테이너 백그라운드 실행
- `level4.py`: 컨테이너 로그 확인
- `level5.py`: 호스트 디렉토리 볼륨 마운트 실행

---

이 저장소는 Python 기본 문법을 공부하면서 실전 운영 기술과 연계된 예제를 익히기 위한 구조로 만들어졌.
