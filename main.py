from func import *
import time

mess={'хай', 'привет', 'здарова', 'здаров', 'ghbdtn', '[fq', 'hay', 'hello', 'хело', 'хелло', 'хеллоу', 'хелоу', 'хей', 'здрасте', 'здрасть', 'здраст', 'эй', 'приветики', 'пивет', 'здравствуйте', 'здравствуй', 'здраствуй', 'здраствуйте', 'добро пожаловать', 'рад познакомиться', 'будем знакомы', 'хой', 'хеу'}

first={'лево', '1', 'левая', 'левый', 'левой', 'один', 'первая', 'первый' 'первой', 'адин', 'одын', 'адын', 'лев', 'first', 'one', '1\'st', '1st', 'ван', 'left', 'фёрст', 'ферст'}

second={'право', '2', 'правая', 'правый', 'правой', 'два', 'вторая', 'второй', 'дво', 'ту', 'секонд', 'прав', 'second', '2\'nd', '2nd', 'right', 'секанд'}

char='йцукенгшщзхъёфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm1234567890'

def how(cont):
	cont=list(cont)
	for i in range(len(cont)):
		if cont[i] not in char:
			cont[i]=' '

	n=0
	for i in str().join(cont).split():
		if i in first:
			if n!=2:
				n=1
			else:
				n=0
				break
		elif i in second:
			if n!=1:
				n=2
			else:
				n=0
				break

	return n

while True:
	for i in read():
		text=how(i[1].lower())
		if text==1:
			send(i[0], 1)
		elif text==2:
			send(i[0], 2)
		else:
			send(i[0], 'Бред какой-то написал')
	time.sleep(1)