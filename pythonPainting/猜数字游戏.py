# 这是一个猜数字的游戏
import random
secretNumber=random.randint(1,20)
print('我会想一个1到20之间的数')
# 共有六次机会猜数字
for i in range(1,7):
	print('输入你的猜测数字：')
	guess=int(input())

	if guess<secretNumber:
		print('你猜测的数字偏小')
	elif guess>secretNumber:
		print('你猜测的数字偏大')
	else:
		break
if guess==secretNumber:
	print('做得好！你总共猜测了'+str(i)+'次')
else:
	print('很遗憾，你失败了。我所想的数字是'+str(secretNumber))
input()
