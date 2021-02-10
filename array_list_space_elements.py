import array as arr
num=[]
num=input().split()
for i in range(0, len(num)): 
    num[i] = int(num[i]) 
num_arra = arr.array('i', num)
for x in range(0, len(num_arra)):    
   if num_arra[x]%10!=4:
        print(num_arra[x],' ',end="")
