n = int(input("Enter any integers : "));

#initialization
y = 0;
tmp = n;
while(n!=0):
    i = int(n%10);
    y = int(y*10 + i);
    n = int(n/10);

print(y);
#checking palindrome or not
if(tmp == y):
    print("Palindrome number", tmp);
else:
    print("Not palindorme number : ",tmp);
