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