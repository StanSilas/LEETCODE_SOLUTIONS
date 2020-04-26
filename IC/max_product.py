# Given a list of integers, find the highest product you can get from three of the integers.

list_of_ints = [ 1, 1, 8, 9, 4]

def highest_product(mylist):
  sorted_list = list_of_ints.sort(reverse = True)
  return list_of_ints[0]*list_of_ints[1]*list_of_ints[2]

print (highest_product(list_of_ints))
