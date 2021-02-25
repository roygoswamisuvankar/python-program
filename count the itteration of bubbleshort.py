import array as arr
list = input().split()
count = 0
for i in range(len(list)):
    for j in range(len(list)-1):
        if(list[j]>list[j+1]):
            tmp = list[j]
            list[j]=list[j+1]
            list[j+1]=tmp;
            count = count + 1

print(count)
