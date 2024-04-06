# Heap/Priority Queue

## Basic Principles
- Heaps in python made with heapify() are min heaps
- We can make them max heaps by inverting the whole array (if its a number) to make a max heap
- heappush = push into heap and maintain heap form
- heappushpop = pushes this value and pops the first value, maintaining heap

### Kth Largest Element in Stream
- init
    - Get the first k elements of nums and heapify it
    - For the rest of the elements in k
    - If the element is larger than the first element of the heap, remove it and add the element
    - Remember python is a **min heap**
- Adding
    - If there aren't k elements in the heap yet, add directly to heap
    - Otherwise, if this element is larger than first element [...]
    - Since we have a min heap of 7 that stores the 7 largest elements in the array, the 1st element is the kth smallest

### Last Stone Weight
- Construct max heap by mutliplying all weights by -1 and heapifying
- Insert -1 * the weights of the heappops
- Return -1 * the last stone

### K Closest Points to Origin
- Maintain the heap by pushing a tuple of the (distance, (x, y))
- Use nsmallest heap function to grab the k closest points and return only the points

