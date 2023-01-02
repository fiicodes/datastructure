def perf(n):
    s=0

    for i in range(1,n):
        if n%i==0:
            s+=i

    if s==n:
        return True
    else:
        return False
print(perf(28))
