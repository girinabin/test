def factor(n):
    for num in range(1,n+1):
        if n%num==0:
            yield num
for num1 in factor(20):
    print(num1)
