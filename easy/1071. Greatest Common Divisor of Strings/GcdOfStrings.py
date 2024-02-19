# import the gcd function
from math import gcd 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check if the one of the strings is concatenated within the other
        if str1 + str2 != str2 + str1:
            # if no, return an empty string
            return ''
        # if yes, pass the lengths of both strings to the gcd function
        gcd_length = gcd(len(str1), len(str2))
        # return the part of str1, that is gcd_length long
        return str1[:gcd_length]  

s = Solution()
print(s.gcdOfStrings('ABAB', 'ABABAB'))