"""
AWS 예제 - 난이도 1
힌트: boto3 설치 필요 (pip install boto3), AWS 자격증명 필요
"""

# [예제]
# 아래 코드는 AWS S3에 저장된 버킷 목록을 출력합니다.
# (AWS 계정 정보가 필요합니다)

import boto3

# 세션 생성 (기본 프로필 사용)
s3 = boto3.client('s3')

# 버킷 목록 가져오기
response = s3.list_buckets()

# 버킷 이름 출력
for bucket in response['Buckets']:
	print(bucket['Name'])

# [풀이 설명]
# boto3.client('s3')로 S3 서비스에 접근합니다.
# list_buckets()로 모든 버킷 정보를 받아옵니다.
# 반복문으로 각 버킷의 이름을 출력합니다.

# [응용문제]
# 1. 버킷 이름만 한 줄에 하나씩 파일(bucket_list.txt)로 저장해보세요.
# 2. 버킷이 하나도 없을 때는 'No buckets found'를 출력하도록 수정해보세요.

import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

if not response['Buckets']:
    print('No buckets found')
else:
    for bucket in response['Buckets']:
        print(bucket['Name'])


# do-not-delete-ssm-diagnosis-932174038447-ap-northeast-2-bkryn 버킷에 파일명 조회

import boto3
s3 = boto3.client('s3')
bucket_name = 'do-not-delete-ssm-diagnosis-932174038447-ap-northeast-2-bkryn'
response = s3.list_objects_v2(Bucket=bucket_name)   
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print('No objects found in the bucket.')

