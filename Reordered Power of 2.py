# Leetcode Name: Reordered Power of 2
# Leetcode Link: https://leetcode.com/problems/reordered-power-of-2/
# Category: Math, Hashing, String, Counting


import math


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        '''
        So there are multiple ways to do this one. All of them take O(1) technically cause u run it fror a set amount of time only. 

        Basic inspiration for this question is the group anagrams question. 

        Cause if u try to find all the permuations of the number of digits like if n = 512 
        then we would have to check 
        215
        251
        125
        152
        521
        512

        which could leave to n! factoriakl time. 
        Instead think of this, if you have all the numbers that are power of 2 then you have somethign like this 
        2
        4
        8
        16
        32
        64
        128
        216
        512
        1024
        2048
        4096

        yiu basically convert all these numbers into a frequency count of the digit and then store it in a map. 

        You also convert your input number into this frequency map and then you can go ahead and convert it. 

        Then in your map you just check if this conversion exists or not. 

        So this way you can use this cod, store the ocnversions once and then just when u are converting your input into frequency number which will take logn time, where n is the number of digits and at max you will have 10 digits so then your time compelxity for that is log 10 which is ficed so the whole time compelxity is then O(1) time. 

        You could do string frequency tuples like group anagrams question there are multiple approaches but I think this is the cleanest cause u do not need to convert it into anything and keeo the numnber int. 

        Time Complexity: O(1) as we are only checking for a fixed number of powers of 2
        Space Complexity: O(1) as we are only storing a fixed number of powers of 2
        
        Ok, so now lets code! 
        '''

        storage = set()

        def getFreq(num):
            newNum = 0

            while num: 
                digit = num % 10
                newNum += math.pow(10, digit)
                num = num // 10
            
            return newNum
        

        for i in range(30):
            storage.add(getFreq(math.pow(2, i)))
        
        inp = getFreq(n)
        return inp in storage 