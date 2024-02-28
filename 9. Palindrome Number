#Simply start at the end of the list and the start of the list with double pointers to check if they are the same, returning false if they are different and watch out for empty string edge case
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        number = str(x)
        j = len(number)-1
        i=0
        while i<j+1:
            if number[i]==number[j]:
                i+=1
                j-=1
            else:
                return False
        
        return True
