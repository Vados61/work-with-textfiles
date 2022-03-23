def creat_union_file():
	union = []
	with open('1.txt', encoding= 'utf-8') as file:
		union.append(file.readlines())

	with open('2.txt', encoding= 'utf-8') as file:
		union.append(file.readlines())

	with open('3.txt', encoding= 'utf-8') as file:
		union.append(file.readlines())

	with open('union.txt', 'w', encoding= 'utf-8')	as file:
		for texts in union:
			for string in texts:
				file.write(string)
			file.write('\n')
			
creat_union_file()
