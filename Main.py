#ls is a list in which user enter the elements
ls=[]
a=input("Enter a Elements into list on by one,Press 'q' to stop: ")
while(a!="q"):
    ls.append(int(a))
    a=input("Enter a Elements into list on by one,Press 'q' to stop: ")
    
print(ls)
#Now We have the List By User
#lets run the list an remove the negative values

#lets take the other list which is for postive
ls2=[]
for i in ls:
    if(int(i)>0):
        ls2.append(i)
    
print(ls2)     
