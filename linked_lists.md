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



