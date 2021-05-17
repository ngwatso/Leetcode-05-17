class Solution:
    def toLowerCase(self, str: str) -> str:
        
        import string

        upper = list(string.ascii_uppercase)
        lower = list(string.ascii_lowercase)

        newStr = ""

        for char in str:
            if char in upper:
                x = upper.index(char)
                newStr += lower[x]
            else:
                newStr += char

        return newStr        
        
'''

U:

"HI"
output = "hi"

"HoW ArE yOu"
output = "how are you"

P:

create lists for upper and lower case characters, iterate through str, if char is in list_1(upper), find index in list_2(lower), add to newStr.  Otherwise, 


'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        x = 33

        count = 0

        while x >= 1:
            x -= 1
            if n < 2**x:
                continue
            else:
                n = n - 2**x
                count += 1

        return count
        
        
'''

U:

32
binary = 00000000000000000000000000100000
output = 1

650
binary = 00000000000000000000001001111010
output = 6

528.64.32.16.8.2

P:

create array that represents 32 bit binary, take input, iterate trhough binArr; when a number can be subtracted and keep input >= 0, binStr += '1', else, binStr += '0'.  count "1"s in binStr.

'''