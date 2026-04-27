"""
AWS 예제 - 난이도 2
힌트: S3 버킷 이름과 업로드할 파일 경로를 지정해야 합니다.
"""

# [예제]
# 아래 코드는 test.txt 파일을 지정한 S3 버킷에 업로드합니다.
# (AWS 계정 정보와 S3 버킷이 필요합니다)
"""
import boto3

bucket_name = 'do-not-delete-ssm-diagnosis-932174038447-ap-northeast-2-bkryn'  # 여기에 본인 버킷 이름 입력
file_path = 'test.txt'            # 업로드할 파일 경로
object_name = 'test.txt'          # S3에 저장될 이름

s3 = boto3.client('s3')
s3.upload_file(file_path, bucket_name, object_name)
print(f"{file_path} 파일이 {bucket_name} 버킷에 업로드되었습니다.")

# [풀이 설명]
# upload_file(로컬파일, 버킷명, S3저장명) 형식으로 사용합니다.
# 파일이 정상적으로 업로드되면 완료 메시지를 출력합니다.

# [응용문제]
# 1. 업로드가 성공했는지 try-except로 예외처리해보세요.
# 2. 업로드할 파일 이름을 사용자 입력(input)으로 받아보세요.
import boto3

bucket_name = 'do-not-delete-ssm-diagnosis-932174038447-ap-northeast-2-bkryn'  # 여기에 본인 버킷 이름 입력
file_path = input("업로드할 파일 경로를 입력하세요: ")  # 사용자 입력으로 파일 경로 받기
object_name = file_path.split('/')[-1]  # 파일 이름을 S3 저장 이름으로 사용 

s3 = boto3.client('s3')
try:
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"{file_path} 파일이 {bucket_name} 버킷에 업로드되었습니다.")
except Exception as e:
    print(f"파일 업로드 중 오류가 발생했습니다: {e}")   
    
# do-not-delete-ssm-diagnosis-932174038447-ap-northeast-2-bkryn 버킷에 파일명 조회 및 삭제
"""
import boto3
s3 = boto3.client('s3')
bucket_name = 'do-not-delete-ssm-diagnosis-932174038447-ap-northeast-2-bkryn'
response = s3.list_objects_v2(Bucket=bucket_name)   
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print('No objects found in the bucket.')


import boto3
s3 = boto3.client('s3')
bucket_name = 'do-not-delete-ssm-diagnosis-932174038447-ap-northeast-2-bkryn'
object_name = input("삭제할 파일 이름을 입력하세요: ")  # 사용자 입력으로 삭제할 파일 이름 받기
try:
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    print(f"{object_name} 파일이 {bucket_name} 버킷에서 삭제되었습니다.")
except Exception as e:
    print(f"파일 삭제 중 오류가 발생했습니다: {e}")
