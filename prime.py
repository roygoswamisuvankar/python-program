n = int(input("Enter a number : "));
flag = 0;
for i in range(2, int(n/2)):
    if(n%i == 0):
        print("Not prime Number");
        flag = 1;
        break;

if(flag == 0):
    print("Prime Number");
