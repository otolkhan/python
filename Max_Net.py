def winner_takes_all(my_list):  
    array=[]
    for i in range(0,len(my_list)):
        if my_list[i]>0:
            array.append(i)
    return array
m=0     
delta=0
y_in=[0] 
epoch=0    
m=int(input("Enter no of Neurons: "))
delta=float(input("Enter weight: "))
y_in=y_in*m
for i in range(m):
    e=float(input("Enter initial value: "))
    y_in[i]=e
    
while True:
    
    y_out=[]
    for i in range(0,m):    
        if y_in[i]>=0:
            y_out.append(y_in[i])
        else:
            y_out.append(0)
    if len(winner_takes_all(y_out))==1:
        print('winner is unit : ',winner_takes_all(y_out)[0]+1) 
        break
    for i in range(0,m):
        
        y_in[i]=y_out[i]-(sum(y_out)-y_out[i])*delta
        result=y_in[i]
        if (result<=0):
            print(f"A({i+1})0",end =" ")
        else:
            print(f"A({i+1}){round(result,2)}",end=" ")
    if epoch==100:
        break
    print("\n")
    epoch+=1
print(f"Total Epoch= {epoch}")  

