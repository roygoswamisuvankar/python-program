import array as arr
list = input().split()
#for i in range(len(list)):
    #for j in range(len(list)-1):
        #if(list[j]>list[j+1]):
         #   tmp = list[j]
          #  list[j]=list[j+1]
           # list[j+1]=tmp;
list.sort()
for i in range(0, len(list)):
    list[i] = int(list[i])
length = len(list)
sum = list[0] + list[length-1]
print(sum)
