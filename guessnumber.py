import random

start = int(input('請決定隨機數開始值： '))
end = int(input('請決定隨機數結束值： '))
answer = random.randint(start, end)

count = 1
while True:
	print('開始第', count, '次猜測')
	guess = int(input('請猜一個數字: '))
	if guess == answer:
		print('猜對了！')
		break
	elif guess < answer:
		print('比答案小')
	elif guess > answer:
		print('比答案大')
	count += 1


