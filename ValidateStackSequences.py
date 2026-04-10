class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        1. can only pop if it is inside the q and can only pop it if it is the last element 
        2. return false if it is inside the stack but not the last element 
        3. if it is not inside then push inside from the pushed list till it meatches that element
        '''

        stackSet = set()
        stack = []
        index = 0
        n = len(pushed)

        for num in popped:
            if num in stackSet and stack[-1] == num: 
                stack.pop()
                stackSet.remove(num)
                continue 
            
            elif num in stackSet and stack[-1] != num: 
                return False 
            
            else: 
                while index < n and num not in stackSet: 
                    stackSet.add(pushed[index])
                    stack.append(pushed[index])
                    index += 1
                
                stackSet.remove(num)
                stack.pop()
        return True 
