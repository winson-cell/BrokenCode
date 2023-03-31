def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    

    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    merged_arr = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1
    
    # Add any remaining elements
    merged_arr += left_half[i:]
    merged_arr += right_half[j:]
    
    a=2;b=3;c=0
    if a>b:
        c=a-b
    else:
        c=b-a
        print("The value of c is: ", c)

    return merged_arr

if __name__ == '__main__':
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = merge_sort(my_list)
    print(sorted_list)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
