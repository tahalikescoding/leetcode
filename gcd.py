#GCD

def gcd(a,b):
    if b>a:
        a,b=b,a
    if b == 0 :
        return a
    a-=b
    if b >a:
        a,b = b,a
    return gcd(a,b)

print(gcd(18,12))