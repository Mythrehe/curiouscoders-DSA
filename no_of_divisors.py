#https://www.geeksforgeeks.org/problems/number-of-divisors1631/1?

class Solution:
    def countDivisors(self, n):
        count = 0
        for i in range(1,n+1):
            if(n%i==0):
                if(i%3==0):
                    count=count+1
        return(count)
