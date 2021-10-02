import random

answer = random.randint(1, 100)

count = 1
while True:
	print('開始第', count, '次猜測')
	guess = int(input('請猜一個數字(1~100): '))
	if guess == answer:
		print('猜對了！')
		break
	elif guess < answer:
		print('比答案小')
	elif guess > answer:
		print('比答案大')
	count += 1


