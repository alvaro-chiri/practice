class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        x_reverse = x_string[::-1]
        if x < 0:
            return False
        else:
            if x_string == x_reverse:
                return True
            else:
                return False
        