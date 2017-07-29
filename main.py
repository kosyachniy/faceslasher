from func import *
import time, os 

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

#'Кто больше нравится?'
kol=len(os.listdir('data'))

while True:
	for i in read():
		name='db/'+str(i[0])+'.txt'
		if not os.path.exists(name):
			with open(name, 'w') as file:
				print(1, file=file)
		with open(name, 'r') as file:
			a=file.read().split('\n')
			nom=len(a)

		if nom>kol:
			send(i[0], 'Ты уже всех оценил..')
		else:
			#send(i[0], '', [get(nom-1), get(nom)])

			#b interval shift t j
			if i[0] not in pe: pe[i[0]]=[nom, len(a), 0, 0, 0]

			pe[i[0]][3]=pe[i[0]][1]%2
			pe[i[0]][1]//=2
			pe[i[0]][4]=(pe[i[0]][1])+pe[i[0]][3]

			print(nom, get(int(pe[i[0]][4]+pe[i[0]][2]-1)))
			send(i[0], '', [get(int(a[pe[i[0]][4]+pe[i[0]][2]-1])), get(nom)])
			text=how(i[1].lower())

			if text==1:
				pe[i[0]][2]+=pe[i[0]][4]
				if pe[i[0]][1]<1:
					a.append(nom)
					for j in range(pe[i[0]][2]+1, len(a))[::-1]:
						a[j], a[j-1]=a[j-1], a[j]
					with open(name, 'w') as file:
						for j in a:
							print(j, file=file)
			elif text==2:
				if not pe[i[0]][3]: pe[i[0]][1]-=1
				if pe[i[0]][1]<1:
					a.append(nom)
					for j in range(pe[i[0]][2]+1, len(a))[::-1]:
						a[j], a[j-1]=a[j-1], a[j]
					with open(name, 'w') as file:
						for j in a:
							print(j, file=file)
			else:
				send(i[0], 'Бред какой-то написал')
	time.sleep(1)