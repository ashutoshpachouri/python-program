for n in range(1,1001):
	n=str(n)
	pw = len(n)
	s=0
	for i in n:
		s+=int(i)**pw
	if int(n) == s:
		print('armstrong number',s)
	

