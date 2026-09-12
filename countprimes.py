#LEETCODE 204: COUNT PRIMES UPTO N

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True]*n
        if n == 0 or n == 1:
            return 0
        prime[0] = False
        prime[1] = False

        for i in range(1,int(n**0.5)+1):
            if prime[i]:
                for j in range(i+i ,n, i):
                    prime[j] = False
        return sum(prime)
        