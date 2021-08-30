def myfactorial(n):
    if(n == 0):
        return 1;
    else:
        return n*myfactorial(n-1);

a = int(input("Enter a number : "));
print(myfactorial(a));