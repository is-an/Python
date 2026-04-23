"""
Docker 예제 - 난이도 5
힌트: volumes 파라미터를 사용해 호스트 디렉토리를 마운트할 수 있습니다.
"""

# [예제]
# 아래 코드는 호스트의 /tmp 디렉토리를 컨테이너의 /data에 마운트합니다.

import docker

client = docker.from_env()
container = client.containers.run(
	'nginx',
	detach=True,
	volumes={'/tmp': {'bind': '/data', 'mode': 'rw'}}
)
print(f"컨테이너 {container.name}가 /tmp를 /data로 마운트하여 실행되었습니다.")

# [풀이 설명]
# volumes 파라미터로 호스트 디렉토리를 컨테이너 내부에 마운트할 수 있습니다.
# bind는 컨테이너 내부 경로, mode는 읽기/쓰기 권한입니다.

# [응용문제]
# 1. 마운트할 호스트 디렉토리와 컨테이너 경로를 사용자 입력으로 받아보세요.
# 2. 컨테이너 실행 후 /data 경로에 test.txt 파일을 생성하는 코드를 작성해보세요.
