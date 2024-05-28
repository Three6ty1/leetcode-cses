# Basic Principles


### Course Schedule
- O(n + p)
  - N nodes that are visited once and checked off so there isn't additional processing
  - P for every edge/prerequisite
- Set up a map of the i course and its prerequisite array
- visitedSet that keeps track of the nodes in the current **DFS/Backtracking**
- Base cases
  - Course we're currently on is in the visited set, return False
  - Course we're currently on has no prerequisites in the map (empty array []), return True
- For each prerequisite run dfs on the course and return False early
- If the course doesn't return early, we remove it from visited for backtracking
- Set the prerequisite map for that node to empty to reduce computation time
- Run the dfs starting from every course since the graph might be disconnected

### Accounts Merge
- 3 steps
- Enumerate through accounts and create a mapping of email -> [accounts]
  - "email@email.com": [1, 2]
  - means email is present in accounts index 1 and 2
- Write dfs(acc, emails) where emails is the current path
  - Check that acc is not in visited
  - Add acc to visited
  - For each email in the acc
    - Add to the current emails
    - For every neighbour of the current email that we created using the mapping, dfs throguh those with the current path
- Run dfs for every account, skipping it if its visited
- Append emails to res after dfs with the name

### Minimum Height Trees
- Build adjacency matrix
  - Adjacency matrix will keep track of which nodes have a degree (how many nodes connected to it) of 1 (leaf node)
- Check for edge case where n = 1
- Get all the leaf nodes by looking at adjanceny matrix degree

- The main thing is a BFS where we prune the leaf nodes from outside in.
- 1 - 2 - 3 - 4 - 5
- 2 - 3 - 4
- 3
- Therefore 3 is the root of a minimum height tree
- The total node count keeps track of the nodes that we're looking at. If this is < 2 then both of these are the root
- 1 - 2 - 3 - 4
- 2 - 3
- For all leaf nodes in this iter
  - Pop the neighbour of this leaf node
  - Remove the leaf node from the neighbours adjacency matrix
  - If the length of the neighbour adjacency matrix becomes 1, it has become a new leaf node
    - Add to BFS queue
  - Replace the next iter with the BFS queue
- Final leave nodes are the minimum sub tree