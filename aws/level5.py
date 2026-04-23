"""
AWS 예제 - 난이도 5
힌트: Lambda 함수 생성 후 S3 트리거 연결은 IAM 권한이 필요합니다.
"""

# [예제]
# 아래 코드는 Lambda 함수를 생성하는 기본 예시입니다.
# (실제 배포에는 IAM 권한, S3 버킷, Lambda 실행 코드 등이 필요합니다)

import boto3

lambda_client = boto3.client('lambda', region_name='ap-northeast-2')

# 실제로는 함수 코드(zip 파일)와 역할(ARN) 등이 필요합니다.
# 아래는 구조 예시입니다.
# response = lambda_client.create_function(
#     FunctionName='MyFunction',
#     Runtime='python3.9',
#     Role='arn:aws:iam::123456789012:role/lambda-role',
#     Handler='lambda_function.lambda_handler',
#     Code={'ZipFile': open('function.zip', 'rb').read()},
#     Description='S3 트리거 예제',
#     Timeout=10,
#     MemorySize=128
# )

# [풀이 설명]
# create_function()에 함수명, 런타임, 역할, 핸들러, 코드 등 필수 정보를 입력해야 합니다.
# 실제로 S3 트리거를 연결하려면 S3 이벤트와 Lambda를 연결하는 추가 작업이 필요합니다.

# [응용문제]
# 1. Lambda 함수 생성 후 S3 버킷 이벤트와 연결하는 코드를 찾아보고 추가해보세요.
# 2. Lambda 함수 목록을 조회해 함수 이름만 출력해보세요.
