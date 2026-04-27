"""
AWS 예제 - 난이도 3
힌트: EC2 인스턴스 정보를 조회하려면 올바른 region을 지정해야 합니다.
"""

# [예제]
# 아래 코드는 EC2 인스턴스의 ID와 상태를 출력합니다.
# (AWS 계정 정보와 EC2 인스턴스가 필요합니다)

import boto3

ec2 = boto3.client('ec2', region_name='ap-northeast-2')  # region은 상황에 맞게 변경
response = ec2.describe_instances()

for reservation in response['Reservations']:
	for instance in reservation['Instances']:
		print(f"ID: {instance['InstanceId']}, 상태: {instance['State']['Name']}")

# [풀이 설명]
# describe_instances()로 모든 인스턴스 정보를 받아옵니다.
# 반복문을 통해 각 인스턴스의 ID와 상태를 출력합니다.

# [응용문제]
# 1. 상태가 'running'인 인스턴스만 출력해보세요.
# 2. 인스턴스의 Public IP도 함께 출력해보세요.

import boto3

ec2 = boto3.client('ec2', region_name='ap-northeast-2')  # region은 상황에 맞게 변경
response = ec2.describe_instances()

for reservation in response['Reservations']:
	for instance in reservation['Instances']:
		if instance['State']['Name'] == 'running':
			public_ip = instance.get('PublicIpAddress', 'N/A')  # Public IP가 없는 경우 'N/A'로 표시
			print(f"ID: {instance['InstanceId']}, 상태: {instance['State']['Name']}, Public IP: {public_ip}")