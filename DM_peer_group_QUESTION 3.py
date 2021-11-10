def finitelist(arrayA, arrayB):
  list_difference = []
#Code for question 2 subquestion 1
  is_subset = all(item in arrayA for item in arrayB)
  if is_subset is True:
    print("B is a subset of A")
  else:
    print("B is not a subset of A")

#Code for question 2 subquestion 2
  for num in arrayA:
    if num not in arrayB:
      list_difference.append(num)
  print(f"A-B = {list_difference}")

#Code for question 2 sub 3
  products = [[val1, val2] for val1 in arrayA for val2 in arrayB ]
  print(f"A x B = {products}")


#Inputs
finitelist([1, 9, 4, 5], [1, 4, 6])
print("\n")
finitelist([2, 6, 10, 14, 22],[3, 9, 11, 17, 15])
