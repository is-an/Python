"""
Docker 예제 - 난이도 1
힌트: docker-py 설치 필요 (pip install docker)
"""

# [예제]
# 아래 코드는 docker-py를 사용해 로컬 Docker 컨테이너 목록을 출력합니다.

import docker

client = docker.from_env()
for container in client.containers.list(all=True):
	print(container.name)

# [풀이 설명]
# docker.from_env()로 Docker 데몬에 연결합니다.
# containers.list(all=True)로 모든 컨테이너 객체를 가져와 이름을 출력합니다.

# [응용문제]
# 1. 실행 중인 컨테이너만 출력해보세요.
# 2. 컨테이너의 상태(status)도 함께 출력해보세요.
