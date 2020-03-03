# link to problem description
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def get_max_sum_hourglass(arr):

    num_rows = len(arr)

    num_cols = len(arr[0])

    hourglass_sum_list = []

    # to iterate through each row and col
    for row in range(num_rows):
        for col in range(num_cols): 
            try:
                top = arr[row][col] + arr[row][col+1] + arr[row][col+2]
                mid = arr[row+1][col+1]
                btm = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]  
                hour_glass_sum = top + mid + btm
                hourglass_sum_list.append(hour_glass_sum)
            except IndexError:
                pass

    max_sum = max(hourglass_sum_list)

    return max_sum

# test case
test_matrix = [ [1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0] ]

max_s = get_max_sum_hourglass(test_matrix)

print(max_s)
