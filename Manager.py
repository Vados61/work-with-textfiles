def creat_union_file(files):
	union = []
	for file_name in files:
		with open(file_name, encoding= 'utf-8') as file:
			text = file.readlines()
			# text.append(file_name)
			# # text.append(str(len(file.readlines())))
			# text.append(file.readlines())
			union.append([file_name + '\n', str(len(text)) + '\n'] + text)
			# print(text)
	print(union)
	union.sort(key=len)

	with open('union.txt', 'w', encoding= 'utf-8')	as file:
		for texts in union:
			for string in texts:
				file.write(string)
			file.write('\n')
			
creat_union_file(['1.txt', '2.txt', '3.txt'])
