# LeetCode Problem Link: https://leetcode.com/problems/minimum-genetic-mutation/
# LeetCode Problem: 433. Minimum Genetic Mutation
# Category: String, Breadth-First Search


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # put the start gene in a q
        # check if the current gene is the endgene if yes then return the number of steps it took to get here 
        # modify each character index with each gene
        # check if the modification exists in the bank
        # if yes add it to the q 
        # remove the gene from the bank, will save space instead of having a visited array 
        # O(n) -> time complexity where n is the number of genes in the bank
        # O(n) -> space complexity for the queue in the worst case
        
        genes = ['A', 'C', 'G', 'T']
        bank = set(bank)
        if endGene not in bank:
            return -1
        

        q = deque()
        q.append(startGene)

        steps = 0
        while q:
            n = len(q)
            for _ in range(n):
                currGene = q.popleft()
                if currGene == endGene:
                    return steps 
                

                for i in range(8):
                    for char in genes:
                        modification = list(currGene) #VERY VERY IMPORTANT THIS IS PLACED HERE OR ELSE U ARE MODIFYINF CHARATERS IN AN ALREADY MODIFIED GENE 
                        modification[i] = char
                        newGene = "".join(modification)

                        if newGene in bank:
                            bank.remove(newGene)
                            q.append(newGene)
            steps += 1
        return -1
