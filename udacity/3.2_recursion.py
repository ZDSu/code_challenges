""" Fibonacci iteratively """
"""Javascript
function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }
  var first = 0,
      second = 1,
      next = first + second;
  for (var i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}
"""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    first = 0
    second = 1
    next = first + second
    for i in range(2, position):
        first = second
        second = next
        next = first + second
    return next


"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
