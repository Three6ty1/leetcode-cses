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
- DFS
- Base case is that if not root, or root = p or q, we return the root
  - This is because if p is the root, and we haven't found q yet, q must be in a deeper level therefore p must be the LCA
  - If we are DFS'ing and trying to find the other root, we can pass back up the recursion without looking at children
- If left and right contains a descendant
  - That means p and q are on left or right, and the current node is the LCA
  - Otherwise, one of the other branches must contain p and q, which would be the one that is not none
    - return left or right

### Binary Tree Level Order Traversal
- Keep track of 3 things
  - Final return value which has [[root]] to start
  - The deque that starts with [root]
  - A temp deque to be built within the loop
- Pop the first node out of the Queue
  - Append left and right to temporary
  - Temp stores the values to loop over in the next level
- If Q is empty, that means we've added all the children of this node to the temp queue-
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

### Construct Binary Tree from Preorder and Inorder Traversal
- Preorder traversal will always display the root of the left subtrees first
- Inorder traversal will give the left and right subtrees based around the root index

- Base case where root is None
- The root is preorder.pop(0)
- The index of that in inorder will determine the left and right subtrees
  - root.left = inorder[:root_index] is left subtree
  - root.right = inorder[root_index + 1:] is right subtree
- Recursively solve for left and right
- Need to do it in this order

- Can convert preorder into a deque for cheaper popleft operations
- Can convert inorder into a map
  - Number: index using enumerate
  - But will need to recursively call using l and r indexes
    - Checking for boundary where ind = l and ind = r (the boundaries cross over)
    - Reducing r to root_ind - 1 or Increasing l to root_ind + 1 in each recursive call

### Kth Smallest Element in a BST
- Initialise self.k and self.res
- DFS
  - Base case if root == None or k <= 0
    - Early return if we found it (at k == 0) 
  - DFS left, then decrement k 
  - Check for k == 0
  - DFS right

### Serialize and Deserialize Binary Tree
- Serialize
  - dfs
  - Base case where root == None, return 'x'
  - Otherwise return root.val and then recursion on root.left root.right seperated by "," or any other character
- Deserialize
  - dfs again
  - Split the serialized into an array
  - Keep track of a self.i to iterate over the array
  - If i == len data then we return
  - Get the value and increment i
  - Return if basecase == x
  - Call dfs on left and right

### Word Ladder
- BFS with visited
- The key to this question is creating an adjacency hashmap for a missing letter in a word to the possible outcomes in the wordList
  - For each word, for each index
  - '_ot': ['bot', 'hot', 'lot'], 'h_t': ['hot', 'hat', 'hit'] etc.
  - Use list splicing to exlude a letter word[:i] + "_" + word[i + 1:]
- Another key is to have the tuples in the BFS deque also keep track of the current depth
- Initialise beginWord with depth 1 and + 1 when adding to the deque
- Standard pop left
- For the range in the length of the word, we start replacing that index in the current word with the empty char
- Get all neighbouring words using the hashmap and loop through
  - Check visited
  - If the word is the found word, return the depth + 1
  - Otherwise append neighbour to visited and append to queue with depth + 1
