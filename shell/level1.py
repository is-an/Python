"""
Shell 예제 - 난이도 1
힌트: subprocess.run()을 사용하면 명령 실행 결과를 쉽게 볼 수 있습니다.
"""

# [예제]
# 아래 코드는 'ls' 명령을 실행해 현재 폴더의 파일 목록을 출력합니다.

import subprocess

result = subprocess.run(['ls'], capture_output=True, text=True)
print(result.stdout)

# [풀이 설명]
# subprocess.run()으로 외부 명령을 실행할 수 있습니다.
# capture_output=True로 결과를 받아오고, text=True로 문자열로 변환합니다.

# [응용문제]
# 1. 'ls -l' 명령을 실행해 파일의 상세 정보를 출력해보세요.
# 2. 명령 실행 결과를 파일(list.txt)로 저장해보세요.
