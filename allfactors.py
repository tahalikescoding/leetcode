#FINDING ALL FACTORS OF A NUMBER BY TWO METHODS


def allfactors(x):
    num = x
    factors = [] 
    for i in range(1,num+1):
        if num%i == 0:
            factors.append(i)
    return factors


def allfactors2(x):
    num = x
    factors = set()
    for i in range(1,int(num**0.5)+1):
        if num%i == 0:
            factors.add(i)
            factors.add(num//i)
    return sorted(factors)

print(allfactors2(36))