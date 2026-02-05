# LeetCode Problem Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# LeetCode Problem: 701. Insert into a Binary Search Tree
# Category: Tree, Binary Search Tree, Binary Tree, Recursion
# Difficulty: Medium



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(h), where h is the height of the tree. In the worst case (unbalanced tree), h can be equal to n (number of nodes), making the time complexity O(n). In a balanced tree, h is log(n), making the time complexity O(log n).
# Space Complexity: O(h) due to the recursion stack. In the worst case, the recursion stack can go as deep as the height of the tree.
from typing import Optional
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        The BST rule states that everything to the left of the node should be less than the parent and everything to the right of the node should be more than the parent. 

        now we basically say that if our insertion node is hreater than the current node then insert in the right tree else left tree, once we find an empty spot. Insert it there. 
        '''
        # if the tree does not exist then the the new node we are adding becomes the root 
        if root == None:
            return TreeNode(val)
        
        # if the value to be inserted is greater than the current node's value, we go to the right subtree and insert it their, here u need to have recursive faith that it works 
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        # similarly for left subtree
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        
        return root 
    

'''
TIME COMPLEXITY EXPLANATION: 
What your code is actually doing
if root.val < val:
    root.right = self.insertIntoBST(root.right, val)
elif root.val > val:
    root.left = self.insertIntoBST(root.left, val)
At each node, you do:
One comparison
Decide left OR right
Recurse into exactly one subtree
You never:
visit both left and right
loop over all nodes
backtrack and try another path
So the runtime depends on how many nodes you visit along that single path.
Key idea: You only follow ONE path
Insertion in a BST is like walking down a hallway:
At each door (node), you choose left or right
You stop when you find an empty spot (None)
You never go back up and try the other side
So the number of operations =
👉 number of nodes on that path
That number is the height of the tree.

What is tree height?
Height = longest path from root to a leaf
Let’s see two cases.

Case 1: Balanced BST → O(log n)
Example:
        8
      /   \
     4     12
    / \    / \
   2   6  10 14
If n = 15 nodes:
Height ≈ log₂(15) ≈ 4
Insertion path:
root → child → child → child → insert
So:
~4 comparisons
~4 recursive calls
✅ Time Complexity = O(log n)
Case 2: Skewed BST → O(n)
Example (insert sorted values):
1
 \
  2
   \
    3
     \
      4
       \
        5
Here:
Height = n
You must walk through every node
Insertion path:
1 → 2 → 3 → 4 → 5 → insert
So:
n comparisons
n recursive calls
❌ Time Complexity = O(n)
Why people say “BST insert is O(n)”
Because nothing in your code keeps the tree balanced.
This is not:

AVL Tree
Red-Black Tree
Treap
It’s a plain BST, so worst case matters.
Interviewers always quote worst-case unless stated otherwise, so they say:

BST insertion is O(n) in the worst case
Why it’s NOT always O(n)
Because:
You don’t traverse all nodes
You only traverse one path
That path can be short if the tree is balanced
That’s why the correct statement is:
Time Complexity = O(h)
where h = height of the tree
Then you explain:
Best / average: O(log n)
Worst: O(n)
Space complexity (important!)
Because of recursion:
Stack depth = height of tree
Space = O(h)
O(log n) balanced
O(n) skewed
How to say this perfectly in an interview
“Insertion into a BST takes O(h) time, where h is the height of the tree.
In the worst case of a skewed tree, h = n, so O(n).
In a balanced tree, h = log n, so O(log n).
Since this BST is not self-balancing, we consider the worst case.”
If you want, next we can:
Compare this with AVL / Red-Black
Convert this to iterative
Or dry-run with a concrete example and count operations line by line
wait so the height of a BST is log n 
Great question — and this is the exact point where most confusion happens.
So let’s be very precise.
Is the height of a BST = log n?
❌ Not always.
✅ Only if the BST is balanced.
The height of a BST depends entirely on how it was built.

Two different worlds exist
1️⃣ Balanced BST → height = O(log n)
A BST is balanced when:
Left and right subtrees have roughly the same number of nodes
No long “chains”
Example:
        8
      /   \
     4     12
    / \    / \
   2   6  10 14
If:
n = 15
Height ≈ log₂(15) ≈ 4
So here:
Search / insert / delete = O(log n)
⚠️ But your code does NOT enforce balance.
2️⃣ Regular BST (like yours) → height can be O(n)
Example (insert sorted input):
Insert: 1, 2, 3, 4, 5

1
 \
  2
   \
    3
     \
      4
       \
        5
Now:
n = 5
Height = 5
Operations must walk through every node.
So:

Search / insert = O(n)
The key misunderstanding
People often hear:
“BST operations are O(log n)”
What they really mean is:
“BST operations are O(log n) if the tree is balanced”
But a plain BST:
Has no guarantee of balance
So worst case must be assumed
The golden rule (memorize this)
Height of BST = O(log n) only if the tree is balanced
Otherwise, height = O(n)
That’s why we say:
Time Complexity = O(h)
Not O(log n) automatically.
Why self-balancing trees exist
Trees like:
AVL Tree
Red-Black Tree
They actively rotate nodes to keep:
height ≈ log n
So they guarantee:
Insert / search / delete = O(log n) always
Interview-ready one-liner
If an interviewer asks:
“What is the height of a BST?”
Correct answer:
“In the worst case, a BST can be skewed, so height is O(n).
If the BST is balanced, height is O(log n).”
That answer is 🔥.
'''