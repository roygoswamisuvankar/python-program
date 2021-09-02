n = input().split(" ");
a = list(map(int, n));
print(a);
count = 0;
for i in a:
    if(i%3 == 0 or i%5 == 0):
        count = count + 1;
print(count);