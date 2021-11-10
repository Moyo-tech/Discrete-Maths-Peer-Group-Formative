def testsets(array):
  for elem in array:
    if array.count(elem) > 1:
      return f"False, the set should be: {set(array)}"
    else:
      return True
  if len(array) == 0:
    return f"True, the set is an empty set(null set)"


# def testsets(array):
#   for i in range(0, len(array)):
#     for j in range(i+1, len(array)):
#       if array[i] == array[j]:
#         return f"False, the set should be: {set(array)}"
#       return True




print(testsets([2, 4, 6, 8, 10]))
print(testsets([10, 20, 30, 10, 40, 30, 50, 60, 70, 70, 20]))
print(testsets([0]))
print(testsets([]))
print(testsets(["Alex", "Bob", "Sam", "Brian", "Sam","Mike", "Alex"]))
print(testsets([True, 2, "book", False, 33,  "libary", "encyclopedia", True, 33, "seat"]))

