"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
  if x <= 1:
    return x
  else:
    return foo(x - 1) + foo(x - 2)


def longest_run(mylist, key):
  total = 0
  total2 = 0
  for i in range(len(mylist)):
    if mylist[i] == key:
      total += 1
    else:
      if total > total2:
        total2 = total
      total = 0
  return max(total, total2)


class Result:
  """ done """

  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size  # run on left side of input
    self.right_size = right_size  # run on right side of input
    self.longest_size = longest_size  # longest run in input
    self.is_entire_range = is_entire_range  # True if the entire input matches the key

  def __repr__(self):
    return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def to_value(v):
  """
    if it is a Result object, return longest_size.
    else return v
    """
  if type(v) == Result:
    return v.longest_size
  else:
    return int(v)


def longest_run_recursive(mylist, key):

  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1, 1, 1, True)
    else:
      return Result(0, 0, 0, False)

  # split mylist in half:
  first = mylist[:(len(mylist) // 2)]
  second = mylist[(len(mylist) // 2):]

  # recursively find longest run on each side of mylist:
  result = longest_run_recursive(first, key)
  result2 = longest_run_recursive(second, key)

  # if both halves all match the key, return the longest run which is the sum of both halves:
  if result.is_entire_range and result2.is_entire_range:
    longest = to_value(result) + to_value(result2)
    return Result(longest, longest, longest, True)

  # if one half is entire range, add the other half's size to the longest run of that side:
  else:
    left = result.left_size
    if result.is_entire_range:
      left += result2.left_size
    right = result2.right_size
    if result2.is_entire_range:
      right += result.right_size

  return Result(
      left, right,
      max(result.right_size + result2.left_size, to_value(result),
          to_value(result2)), False)
