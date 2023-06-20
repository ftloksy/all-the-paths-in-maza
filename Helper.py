def isItemInArray(array, item):
  """
  Checks if an item is in an array and returns True if it is, False otherwise.

  Args:
    array: The array to search.
    item: The item to search for.

  Returns:
    True if the item is in the array, False otherwise.
  """

  for i in range(len(array)):
    if array[i] == item:
      return True

  return False