T=()
while 1:
       item= input('enter the item')
       T = T + (item,)
       c = input('do you want to continue')
       if c.lower()=='yes':
              break
print(T)
