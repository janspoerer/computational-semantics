array = [7, 5, 3, 2, 6, 8, 9, 1, 1]

def splitting_into_pairs( array ):
    middle_index = len(array)//2
    left_array = array[:middle_index]
    right_array = array[middle_index:]
    if middle_index > 2:
        left_array = splitting_into_pairs(left_array)
        right_array = splitting_into_pairs(right_array)
    #elif middle_index == 3:
    #    x = 
    #    y
    #    right_array = right_array//2
    return [left_array, right_array]

# def merge_pairs( pairs )
#     pairs[0]
#     pairs[1]

pairs = splitting_into_pairs( array )
# result = merge_pairs( pairs )

# print(type(result))
# print( result )

print(type(pairs))
print( pairs )




# If odd number: you leave one that you don't sort

# recursive functions

# //

# dividing data sets
# comparing

# [[],[]]

# def split_into_pairs_of_two ( array ):
#     length = len( array )
#     length_first_array = length // 2
#     for i in 0 to length_first_array
#         first_array = array.pop(i)

#     if length < 2:
#         print ("Array too small. Min of 2 numbers needed.")
#     elif:


# def merge_sort:
#     splitted_array = split_into_pairs_of_two ( array )
#     [[7,5],[3,2]]
#     compare_two_numbers ( first, second )
#         return 0 or 1
