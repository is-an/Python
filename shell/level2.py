"""
Shell 예제 - 난이도 2
힌트: 명령 결과를 변수로 받아오려면 capture_output=True 옵션을 사용하세요.
"""

# [예제]
# 아래 코드는 'pwd' 명령을 실행해 현재 작업 디렉토리를 출력합니다.

import subprocess

result = subprocess.run(['pwd'], capture_output=True, text=True)
print('현재 디렉토리:', result.stdout.strip())

# [풀이 설명]
# 'pwd' 명령은 현재 디렉토리 경로를 출력합니다.
# result.stdout.strip()으로 줄바꿈을 제거합니다.

# [응용문제]
# 1. 사용자에게 명령어를 입력받아 실행 결과를 출력하는 코드를 작성해보세요.
# 2. 명령 실행이 실패했을 때 에러 메시지를 출력하도록 해보세요.
