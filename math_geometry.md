# Math and Geometry

### Spiral Matrix
- Keep track of top right down left in terms of their boundaries to the matrix
  - n - 1 m - 1
- Loop while the boundaries dont overlap
- For each direction, loop from the starting to the end boundary
  - Make sure to do -1 or +1 since for range is not inclusive
- Increment or decrement the axis/edge that is static
- Return 0:m*x as the loop continues past the boundaries

### Basic Calculator
- Recursive solution
- 2 stacks (one implicit due to recursion) and one to keep track of the current values
- Update function to insert a value with its operator into the stack
- Inside recursive function
  - Have the current num, stack and prev_sign (init to +)
  - While i < n
  - If its a digit, do base 10 increase (num * 10 + int(s[i]))
  - If it is an operator, call update function on num and prev sign
    - Update the sign to the current s[i] and num back to 0
  - If its a bracket, call recursive on i + 1
    - Return the current i as j - 1 (since we calculated all the way past the brackets)
  - If its a closed bracket
    - Update the sign with the previous num
    - Sum the current stack and return it with i + 1
- Update the prev sign, num
- Return sum of stack...

- I wish this was less verbose
