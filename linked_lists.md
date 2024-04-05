# Linked Lists

## Basic Principles
- Have a dummy listnode that the loop adds onto
  - We access the head of the return value by doing dummy.next
- Singly linked lists
  - Val and Next
- Doubly linked lists
  - Prev, Val and Next
- Fast and Slow pointers
  - Fast iterates twice as fast as slow or
  - Fast iterates n times before slow and they move together
  - Used to find cycles within a linked list
  - Used to find the middle of a linked list when fast reaches None, slow = middle

### Reverse Linked List
- Start with prev = None
- Increment through each
- 1 2 3 None
- prev = None
  - 1 > 2 > 3 > None
- curr = head = 1
  - 1(Curr) > 2 > 3 > None
- head = head.next = 2
  - 1(Curr) > 2(Head) > 3 > None
- curr.next = prev = None
  - None(Prev) < 1(Curr)
  - 2(Head) > 3 > None
- prev = curr
  - None < 1(Prev and Curr)
  - 2 (Head) > 3 > None

- While head
- Increment curr up
- Reverse curr by doing curr.next = prev
- Move prev up by doing prev = curr
- Increment head to head.nxet

### Merge Two Sorted Lists
- Dummy head with curr
- While l and r
- Compare the values, and insert.
  - curr = previous iterations value
    - Assign curr.next to r or l
    - On first iter it also assigns dummy.next
    - Then assign this iterations value to curr = l or r
  - Increment l or r with .next
- After the loop is finished, assign curr.next to "l or r" if one of the lists are not None

### Reorder List
- This is from recognising that the solution is essentially splitting the linked list in two, reversing the latter half and then interwining them together
- Find the middle of the linked list using fast slow pointers
- From the middle of the linked list, reverse the second half of the list
- Make sure to assign slow.next = None to prevent a cycle where the end of both lists point to the same element
- Loop through h2 and interweave
  - Store the temp next using nextt = h1.next
  - Reassign h1.next to h2
  - Assign h1 = h2
  - Swap by doing h2 = nextt = original h1.next

### Remove Nth Node From End of List
- Iterate fast n times which means that when fast reaches None, slow is n away from the end
  - If fast reaches None in this loop it means n = len(linkedList) therefore the element to remove is the first of the linked list
- Now since fast = slow + n, iterate both until fast reaches None
- Reassign slow.next to slow.next.next

### Copy List with Random Pointer
- Create a map old-to-new and copy over the linked list into the map
- Iterate through head
  - Access the deep copy of curr by using the map function
  - Assign .next and .random by using curr.next and curr.random within the maps .get
- Return the head of old-to-new

### Add Two Numbers
- Keep track of a carry over value
- Dummy node
- If l1/l2 += onto carry and go to next
- divmod(carry, 10) = carry // 10, carry % 10
- Carry is the remainder of the division
- Value is the modulo
- Insert the value to a new ListNode

### Linked List Cycle
- Fast slow pointers
- Try-Catch while n = n.next and nn = n.next.next

### [Find the Duplicate Number](https://www.youtube.com/watch?v=wjYnzkAhcNk)
- Use slow and fast pointers until we find the cycle
- According to Floyds Cycle detection algorithm, from the start and from where slow == fast
  - When these two pointers increment and intersect, that is where the cycle is from
- Set slow2 = 0
- Increment slow and slow2 until they intersect and return.

### LRU Cache
- Can be done using a hashmap store for O(1), -1 if not in store and an array with pop and append for LRU
  - When we get, we reset the key in the cache by removing it and then appending it back on
  - When we put, we also reset the key in the cache
  - But we also pop the first index (least used) and then set that index in the store as -1
- [Proper Doubly Linked list solution](https://leetcode.com/problems/lru-cache/solutions/45926/python-dict-double-linkedlist/)
  - This just uses a node implementation that does the exact same thing as the array implementation
  - Nice trick used to set a dummy node at the end of head and tail so that whenever we insert, we can assign head and tail to a non None value