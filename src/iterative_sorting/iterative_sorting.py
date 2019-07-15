# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    # Compare two and swap if a > b
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # Find highest number in arr. If any negative numbers, return err:
    hash_length = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if arr[i] > hash_length:
            hash_length = arr[i]
        
    print(f'Hash length should go to {hash_length}')
    # Create hash table with maximum arr values as keys, set to 0
    hash = { i: 0 for i in range(0, hash_length+1)}
    print(hash)

    # In hash, increase count of each instance of i in arr
    for i in range(0, len(arr)):
        hash[arr[i]] += 1
    
    # Add instances in new_arr to find indices of each element in arr
    for i in range(1, len(hash)):
        hash[i] = hash[i] + hash[i-1]

    # Go through arr to place final sorted_arr, decreasing each placed instance
    sorted_arr = [None] * len(arr)
    for i in range(0, len(arr)):
        sorted_arr[hash[arr[i]]-1] = arr[i]

    return sorted_arr


# print(count_sort([2, 5, 3, 7, 6], [0, 1, 2, 3, 4, 5, 6, 7]))
print(count_sort([6, 3, 7, 2, 8, 1, 7, 2]))