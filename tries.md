# Tries

## Basic Principles
- Prefix tree
- Efficiently store and retrieve keys in a dataset of strings
- TrieNode Datastructure
    - Hashmap of Letter -> TrieNode
    - A value that keeps track of if its the end of a string or not
- For each letter in the word were trying to find, check if the current node hashmap contains an entry for it
    - Increment into it like a binary tree
- We can search for a word in the same way, but at the end we need to check if the last letter has the end flag
- Starts with or prefixes use the same algorithm but skips this flag check

### Design Add and Search Words Data Structure
- Use a TrieNode datastructure
- For search, we use a dfs algorithm
    - Base case when the word is empty (we matched to the end)
    - If the letter is "." We do a recursive call on dfs for every letter in the current nodes children
    - If the letter is specified, we check if the letter is in the children
        - If it is we recursive dfs
        - If not we return False
