"""
Docker 예제 - 난이도 4
힌트: 컨테이너 객체의 logs() 메서드를 사용하세요.
"""

# [예제]
# 아래 코드는 실행 중인 모든 컨테이너의 로그를 출력합니다.

import docker

client = docker.from_env()
for container in client.containers.list():
	print(f"컨테이너: {container.name}")
	print(container.logs().decode())

# [풀이 설명]
# containers.list()로 실행 중인 컨테이너를 가져옵니다.
# logs() 메서드로 로그를 받아와 출력합니다.

# [응용문제]
# 1. 특정 이름을 가진 컨테이너의 로그만 출력해보세요.
# 2. 최근 10줄만 출력하도록 수정해보세요.
