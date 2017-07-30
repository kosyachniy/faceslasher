from func import *
import time, os

hello={'хай', 'привет', 'здарова', 'здаров', 'ghbdtn', '[fq', 'hay', 'hello', 'хело', 'хелло', 'хеллоу', 'хелоу', 'хей', 'здрасте', 'здрасть', 'здраст', 'эй', 'приветики', 'пивет', 'здравствуйте', 'здравствуй', 'здраствуй', 'здраствуйте', 'добро пожаловать', 'рад познакомиться', 'будем знакомы', 'хой', 'хеу', 'hi', 'helo'}

first={'лево', '1', 'левая', 'левый', 'левой', 'один', 'первая', 'первый' 'первой', 'адин', 'одын', 'адын', 'лев', 'first', 'one', '1\'st', '1st', 'ван', 'left', 'фёрст', 'ферст'}

second={'право', '2', 'правая', 'правый', 'правой', 'два', 'вторая', 'второй', 'дво', 'ту', 'секонд', 'прав', 'second', '2\'nd', '2nd', 'right', 'секанд'}

char='йцукенгшщзхъёфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm1234567890'

def how(cont):
	cont=list(cont)
	for i in range(len(cont)):
		if cont[i] not in char:
			cont[i]=' '

	n=0
	text=str().join(cont).split()
	for i in text:
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
	return n if n else 0

with open('set.txt', 'r') as file:
	kol=len(json.loads(file.read())['image'])

while True:
	for i in read():
		u=i[0]
		name='db/'+str(u)+'.txt'
		if not os.path.exists(name):
			with open(name, 'w') as file:
				print(1, file=file)
		with open(name, 'r') as file:
			a=file.read().split('\n')[:-1]
			nom=len(a)+1

		if nom>kol:
			send(u, 'Ты уже всех оценил..')
			send(u, 'Твой личный рейтинг:')
			for i in range(len(a)):
				send(u, str(i+1)+'-ое место', [get(int(a[i]))])
		else:
			text=how(i[1].lower()) if u in pe else 3
			if text in (1, 2):
				if text==1:
					pe[u][2]+=pe[u][4]
				elif text==2:
					if not pe[u][3]: pe[u][1]-=1
				if pe[u][1]<1:
					a.append(nom)
					for j in range(pe[u][2]+1, len(a))[::-1]:
						a[j], a[j-1]=a[j-1], a[j]
					with open(name, 'w') as file:
						for j in a:
							if j:
								print(j, file=file)
					del pe[u]
					#send(u, 'Следующая девушка!')
				else:
					pe[u][3]=pe[u][1]%2
					pe[u][1]//=2
					pe[u][4]=pe[u][1]+pe[u][3]
					send(u, '', [get(int(a[pe[u][4]+pe[u][2]-1])), get(nom)])
			elif text==3:
				#b interval shift t j
				pe[u]=[nom, len(a), 0, 0, 0]
				
				pe[u][3]=pe[u][1]%2
				pe[u][1]//=2
				pe[u][4]=pe[u][1]+pe[u][3]
				send(u, 'Кто больше нравится?', [get(int(a[pe[u][4]+pe[u][2]-1])), get(nom)])
			else:
				send(u, 'Бред какой-то написал')
	time.sleep(1)