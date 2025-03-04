#https://www.geeksforgeeks.org/problems/prime-number2314/1

class Solution:
    def isPrime(self, n):
        if n<2:
            return("false")
        else:
            is_prime = True
            for i in range(2,n):
                if (n%i==0):
                    is_prime = False
                    break
        
            return(is_prime)
