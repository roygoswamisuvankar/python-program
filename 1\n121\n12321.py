n = int(input())
odd = 1
for i in range(0,n+1):
    k = 0
    for j in range(0,2*i-1):
        if(j<i):
            k = k+1
        else:
            k=k-1
        print(k,end="")
    print()
