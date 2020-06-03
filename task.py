def racialWords():
	with open(filename,'r') as file:
	racialwords=['..','..']
	f=file.readlines()
	for i in f:
		if i not in racialwords:
			return file
		else:
			file.flush()
if __name__=="__main__":
	textedFile=racialwords()
	r=textedFile.read()
	print(r)
