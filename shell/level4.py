"""
Shell 예제 - 난이도 4
힌트: /etc/passwd 파일을 읽어서 사용자 계정 목록을 추출할 수 있습니다.
"""

# [예제]
# 아래 코드는 /etc/passwd 파일에서 사용자 계정 이름만 출력합니다.

with open('/etc/passwd', 'r') as f:
	for line in f:
		if not line.startswith('#'):
			print(line.split(':')[0])

# [풀이 설명]
# /etc/passwd 파일의 각 줄에서 ':'로 구분된 첫 번째 필드가 계정 이름입니다.
# 주석(#)으로 시작하는 줄은 제외합니다.

# [응용문제]
# 1. UID가 1000 이상인 사용자만 출력해보세요.
# 2. 계정 이름을 오름차순으로 정렬해서 출력해보세요.
