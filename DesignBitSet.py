# LeetCode Problem Link: https://leetcode.com/problems/design-bitset/
# LeetCode Problem: 2166. Design Bitset
# Category: Design, Array, Simulation
# Difficulty: Medium

class Bitset:
    '''
    The main idea is to keep track of the flipped state of the bits and the count of ones in the bitset.
    Time Complexity: O(1) for all operations except toString which is O(n) where n is the size of the bitset.
    Space Complexity: O(n) for storing the bits in the bitset.
    
    2 crucial facts to know that 
    XOR with 1 gives a flipped bit 
    1 xor 1 = 0
    0 xor 1 = 1

    XOR with 0 fives the same number 
    1 xor 0 = 1
    0 xor 0 = 0
    '''

    def __init__(self, size: int):
        self.flipped = 0
        self.bits = [0] * size 
        self.n = size
        self.ones = 0 
        

    def fix(self, idx: int) -> None:
        actual = self.bits[idx] ^ self.flipped
        if actual == 0:
            self.bits[idx] ^= 1
            self.ones += 1
        

    def unfix(self, idx: int) -> None:
        actual = self.bits[idx] ^ self.flipped
        if actual == 1:
            self.bits[idx] ^= 1
            self.ones -= 1
        

    def flip(self) -> None:
        self.flipped ^= 1
        self.ones = self.n - self.ones 
        

    def all(self) -> bool:
        return self.n == self.ones
        

    def one(self) -> bool:
        return self.ones > 0
        

    def count(self) -> int:
        return self.ones
        

    def toString(self) -> str:
        cr = [str(b^self.flipped) for b in self.bits]
        return "".join(cr)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()