# GH: vaheandonians

def sort_my_array( array ):
  j = 1
  for j in range(j, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
      array[i + 1] = array[i]
      i = i - 1
    array[i + 1] = key
  return array

array = [7, 2, 9, 4, 3, 1, 6, 5, 8]

sort_my_array(array)

print (array)
