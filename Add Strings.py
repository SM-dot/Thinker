class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''
        Main thing is that allowed to sum int by int 
        If we convert the whole number to int and then do, if we have a very large number that can take up too much space. SO the pointer approach is the best. 

        Edge things to take care of is like having a carry, you need to have a carry to calculate the sum. 

        O(max(n, m)) is time complexity 
        O(n) is space complexity 
        Now let's code 
        '''

        p1, p2 = len(num1) -1, len(num2) -1
        carry = 0
        result = []


        while p1 >= 0 or p2 >= 0 or carry > 0:
            d1 = int(num1[p1]) if p1 >= 0 else 0
            d2 = int(num2[p2]) if p2 >= 0 else 0

            total = (d1 + d2 + carry) % 10
            carry = (d1 + d2 + carry) // 10

            p1 -= 1
            p2 -= 1

            result.append(str(total))
        
        return "".join(result[::-1])
