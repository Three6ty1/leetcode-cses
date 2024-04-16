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