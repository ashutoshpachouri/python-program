a=('prem','rani','ravi','rani','seema','prem')
b=[]
for i in a:
	if a.count(i)>1:
	       if i not in b:
	              b.append(i)
print(b)
		
		
       
