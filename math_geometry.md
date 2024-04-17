# Math and Geometry

### Spiral Matrix
- Keep track of top right down left in terms of their boundaries to the matrix
  - n - 1 m - 1
- Loop while the boundaries dont overlap
- For each direction, loop from the starting to the end boundary
  - Make sure to do -1 or +1 since for range is not inclusive
- Increment or decrement the axis/edge that is static
- Return 0:m*x as the loop continues past the boundaries

