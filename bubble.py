a = [];
tmp = 0;
print("Please enter array elements : ");

#input array elements using for loop
for i in range(0,5):
    i = int(input());
    a.append(i);

print("\nBefore shorting : ");
print(a);

#find the length of array
n = len(a);

#shorting array elements
for i in range(0,n-1):
    for j in range(0, n-i-1):
        if(a[j]>a[j+1]):
            tmp = a[j];
            a[j] = a[j+1];
            a[j+1] = tmp;

print("\nAfter shorting : ");
print(a);
