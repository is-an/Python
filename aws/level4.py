"""
AWS 예제 - 난이도 4
힌트: DynamoDB 테이블 생성 시 파티션키 속성 타입을 지정해야 합니다.
"""

# [예제]
# 아래 코드는 DynamoDB에 'TestTable' 테이블을 생성합니다.
# (AWS 계정 정보와 DynamoDB 사용 권한 필요)

import boto3

dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')

table_name = 'TestTable'

response = dynamodb.create_table(
	TableName=table_name,
	KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
	AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
	ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
)
print(f"테이블 {table_name} 생성 요청 완료")

# [풀이 설명]
# KeySchema와 AttributeDefinitions로 파티션키를 지정합니다.
# create_table() 함수로 테이블을 생성합니다.

# [응용문제]
# 1. 테이블이 이미 존재할 때 예외처리를 추가해보세요.
# 2. 테이블 생성 후 실제로 생성 완료될 때까지 대기하는 코드를 추가해보세요.
