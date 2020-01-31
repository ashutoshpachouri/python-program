n=input('write a number')
pw = len(n)
s=0
for i in n:
	s+=int(i)**pw
if int(n) == s:
	print('armstrong number',s)
else:
	print('not a armstrong')

