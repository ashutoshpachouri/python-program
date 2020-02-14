a=[1,2,3,4,5,(1,2)]
count=0
for i in a:
	if type(i)!=tuple:
		count += 1
	else:
		break
print(count)
