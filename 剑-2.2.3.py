class Solution:
    def addBinary(self, num1, num2):
        res = ''
        i1,i2,carry = len(num1)-1,len(num2)-1,0
        while i1>=0 or i2>=0:
            x = ord(num1[i1])-ord('0') if i1>=0 else 0
            y = ord(num2[i2])-ord('0') if i1>=0 else 0
            sum = x+y+carry
            res += str(sum%2)
            carry = sum//2
            i1 -= 1
            i2 -= 1
        if carry:
            res += str(carry)
        return res[::-1]
