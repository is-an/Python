"""
Docker 예제 - 난이도 2
힌트: client.images.pull('nginx')와 같이 이미지를 받아올 수 있습니다.
"""

# [예제]
# 아래 코드는 docker-py로 nginx 이미지를 다운로드(pull)합니다.

import docker

client = docker.from_env()
image = client.images.pull('nginx')
print('nginx 이미지가 다운로드되었습니다.')

# [풀이 설명]
# images.pull('nginx')로 Docker Hub에서 nginx 이미지를 받아옵니다.
# 다운로드가 완료되면 메시지를 출력합니다.

# [응용문제]
# 1. 이미지 이름을 사용자 입력으로 받아 pull해보세요.
# 2. 다운로드한 이미지의 태그 목록을 출력해보세요.
