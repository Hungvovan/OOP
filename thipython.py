def soluong(n):
    c=0
    while n>0:
        n//=10
        c+=1
    return c

def dequy(n):
    if n<10:
        return 1
    return 1 + dequy(n//10)
 
## Đếm bao nhiêu chữ số trong số

def gt(n):
    kq=1
    for i in range(1,n+1):
        kq*=i
    return kq

def gt(n):
    if n<1:
        return 1
    return n* gt(n-1)
#Giai thua
def chinh(n, k):
    result = 1 
    for i in range(n, n - k, -1):
        result *= i 
    return result

def tohop(n,k):
    result = 1 
    for i in range(n, n - k, -1):
        result *= i 
    for i in range(1,k+1):
        result//=i
    return result




if __name__=="__main__":
    n=int(input())
    print(soluong(n))
    print(dequy(n))