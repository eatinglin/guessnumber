import random

answer = random.randint(1, 100)


while True:
	guess = int(input('請猜一個數字(1~100): '))
	if guess == answer:
		print('終於猜對了！')
		break
	elif guess < answer:
		print('比答案小')
	elif guess > answer:
		print('比答案大')


