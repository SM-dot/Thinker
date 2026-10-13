# Leetcode: Convert Integer to Sum of Two Non-Zero Integers
# Link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Category: Math, Greedy

class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        '''
        See the brute force is simple it is basically just thinking about how we break it up into a and b - a
        So a can be 1, 2, blah blah. The solution would have a time complexity of O(nlogn)

        BUT 

        We can bring it down, we can get it to O(logn)

        Biggest hint to think like this is that the number of digits in any number is equal to log n. 

        So we handle the problem digit wise.

        If the digit we are handling is 1, we do not subtract 1. Cause 1 - 1 = 0, instead we subtract 2 and we get 1 - 2 = 9

        so a = number - whatever value (1 or 2)
        b = b + whatever value we removed 

        if our number is 1023
        we handle 3 
        a = 1023 - 1 = 1022
        b = 1
        nuw we solve 1023 - 1 = 1022 // 10 = 102
        a = 102 - 10(1 * place value) = 1023 - 10 = 1013
        
        The optimal solution is kind of hard, so work thorugh an example to solve it please 
        lass Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        int a = n;
        int b = 0;
        int placeValue = 1;

        //a+b == n
        while(n > 1) {
            int take = 1;

            if(n%10 == 1) {
                take = 2;
            }

            a = a - take*placeValue;
            b = b + take*placeValue;

            n = (n-take)/10; //moving to next digit

            placeValue *= 10;
        }

        return {a, b};

        
    }
};
        '''
        a = n
        b = 0
        placeValue = 1

        while n > 1: 
            take = 1

            if n % 10 == 1:
                take = 2
            
            a = a - take*placeValue
            b = b + take*placeValue

            n = n - take 
            n = n // 10

            placeValue *= 10

        return [a, b]
