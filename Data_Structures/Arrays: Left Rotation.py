# A left rotation operation on an array shifts 
# each of the array's elements 1 unit to the left

# a matter of changing index?

def left_rotation(arr, num_of_rotations):

    for rotation in range(num_of_rotations):

        # save last element as it will be overriden during the first iteration
        # update the last element with every rotation
        last_element = arr[-1]

        for index in range(len(arr)):

            arr[index-1] = arr[index]

            # second last index
            if index == (len(arr) - 1):
                arr[index-1] = last_element

    return arr

# test case
arr = [1,2,3,4,5]

rotated_arr = left_rotation(arr, 2)

assert rotated_arr == [3,4,5,1,2]
