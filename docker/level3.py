"""
Docker 예제 - 난이도 3
힌트: detach=True 옵션을 주면 백그라운드 실행이 가능합니다.
"""

# [예제]
# 아래 코드는 nginx 컨테이너를 백그라운드로 실행합니다.

import docker

client = docker.from_env()
container = client.containers.run('nginx', detach=True)
print(f"컨테이너 {container.name}가 실행되었습니다.")

# [풀이 설명]
# containers.run('nginx', detach=True)로 백그라운드 실행이 가능합니다.
# 실행된 컨테이너의 이름을 출력합니다.

# [응용문제]
# 1. 컨테이너 실행 시 포트(80:8080) 바인딩을 추가해보세요.
# 2. 컨테이너 실행 후 5초 뒤 자동으로 중지(stop)하는 코드를 작성해보세요.
