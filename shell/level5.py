"""
Shell 예제 - 난이도 5
힌트: 'ps' 명령과 'grep'을 조합해 프로세스 존재 여부를 확인할 수 있습니다.
"""

# [예제]
# 아래 코드는 'docker' 프로세스가 실행 중인지 확인합니다.

import subprocess

result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
if 'docker' in result.stdout:
	print('docker 프로세스가 실행 중입니다.')
else:
	print('docker 프로세스가 실행 중이지 않습니다.')

# [풀이 설명]
# 'ps aux' 명령으로 현재 실행 중인 모든 프로세스를 확인합니다.
# 결과 문자열에 'docker'가 포함되어 있으면 실행 중으로 판단합니다.

# [응용문제]
# 1. 사용자에게 프로세스 이름을 입력받아 실행 여부를 확인해보세요.
# 2. 실행 중인 프로세스의 개수를 출력해보세요.
