"""
Shell 예제 - 난이도 3
힌트: 결과 문자열을 split() 등으로 파싱해보세요.
"""

# [예제]
# 아래 코드는 'df -h' 명령을 실행해 디스크 사용량 정보를 출력합니다.

import subprocess

result = subprocess.run(['df', '-h'], capture_output=True, text=True)
print(result.stdout)

# [풀이 설명]
# 'df -h' 명령은 디스크 용량과 사용량을 사람이 읽기 쉬운 단위로 보여줍니다.
# result.stdout으로 전체 결과를 출력합니다.

# [응용문제]
# 1. 각 파일시스템의 사용률(%)만 한 줄씩 출력해보세요.
# 2. 사용률이 80% 이상인 파일시스템만 출력해보세요.
