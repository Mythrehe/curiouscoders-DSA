#https://www.geeksforgeeks.org/problems/sum-of-series2811/1

class Solution:
    def seriesSum(self, n : int) -> int:
        sum=0
        for i in range(1,n+1):
            sum=sum+i
        return sum
