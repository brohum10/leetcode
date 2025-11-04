class Solution:
    def isPalindrome(self, x: int) -> bool:

        
        numReversed = 0
        xHold = x
        
        while(x > 0):

            lastDigit = x % 10 

            numReversed = numReversed * 10 + lastDigit 

            x = x // 10 

        return xHold == numReversed

