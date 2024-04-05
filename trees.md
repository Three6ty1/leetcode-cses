# Trees

## Basic Principles
- It's basically nearly all recursion...
  - Always a base case of not root return
- BFS and DFS
  - DFS Recursive go left then go right
  - BFS is with a queue, loop through the length of the original queue and update it while its going
    - **This might cause problems with python for loops**

### Invert Binary Tree
- Swap root.left with root.right
- Recursively call invertTree

### Maximum Depth of Binary Tree
- Recursively call and return 1 + max(maxDepth(root.left), maxDepth(root.right))

### Diameter of Binary Tree
- Keep track of max diameter in self.diameter
- Get the depth of left and right, and then compare left + right with the current max diameter

### Balanced Binary Tree
- Keep track of if the tree is balanced in self.balanced = True
- If the difference between depth of left and right is > 1 then its unbalanced

### Same Tree
- DFS through both trees at the same time
- If the values are not equal or if one root exists and the other doesn't, return False
- Otherwise return True

### Subtree of Another Tree
- DFS down the entire subtree
- If the root values are equal, run Same Tree for the current root
  - If this is true, return True

### Lowest Common Ancestor of a Binary Search Tree
- Iterative approach
- Get the smaller and larger values of the two nodes to find
- Since BST left = smaller and right = larger,
  - If root.val > large, move left
  - If root.val < small, move right
  - Until the small < root.val < large

### Binary Tree Level Order Traversal
- Keep track of 3 things
  - Final return value which has [[root]] to start
  - The deque that starts with [root]
  - A temp deque to be built within the loop
- Pop the first node out of the Queue
  - Append left and right to temporary
  - Temp stores the values to loop over in the next level
- If Q is empty, that means we've added all the children of this node to the temp queue
  - Append all values of temp into the return array in their own level
  - Assign Q = temp to move down one level
  - Reset temp to an empty deque

### Binary Tree Right Side View
- Level Order Traversal but you only append the last node of every level.
- Instead of using temp and two queues
  - Use a for loop of the range of the original length
  - Append to the original queue
  - **Do not loop over the queue itself**
- Append outside the for loop as node would be assigned the last value


