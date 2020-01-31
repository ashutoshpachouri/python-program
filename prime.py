l=[1,45,3,3,2,3,45,56,4,5,5,57,54,76]
primelist=[]
for num in l:
	if num>1:
		for i in range(2,num):
			if(num%i)==0:
				break
		else:
			primelist.append(num)
print('prime list',primelist)
