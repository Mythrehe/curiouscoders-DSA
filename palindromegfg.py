#https://www.geeksforgeeks.org/problems/palindrome0746/1
class Solution:
    def isPalindrome(self, n):
		sum=0
		rev=n
		while (n>0):
		    ld=n%10
		    sum=sum*10+ld
		    n=n//10
	    return rev == sum
