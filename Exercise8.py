# Learning Data Structures by Building the Merge Sort Algorithm

def merge_sort(array: list):
    """
    Arranges values in order using merge sort

    Args:
        :array: Taking in an array
    """
    # If there's only one element, there's nothing to arrange
    if len(array) <= 1:
        return

    # Figuring out the middle point of the array
    middle_point = len(array) // 2
    # Splitting the array into two parts
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursive calling to reposition the leftmost and rightmost points
    merge_sort(left_part)
    merge_sort(right_part)

    # Setting up left, right, and sorted indexes
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merging the left and right parts
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # If the left part is less than the right part, the left part is placed first
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1 # Incrementing the left index
        else: # Otherwise, the right part is placed first
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1 # Incrementing the right index
        # Incrementing the sorted index
        sorted_index += 1 

    # If there are any remaining elements in the left or right parts
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        # Incrementing the left index
        left_array_index += 1
        # Incrementing the sorted index
        sorted_index += 1

    # If there are any remaining elements in the right part
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        # Incrementing the right index
        right_array_index += 1
        # Incrementing the sorted index
        sorted_index += 1

    return array

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    print(f"Unsorted: {numbers}")
    print(f"Sorted: {merge_sort(numbers)}")
