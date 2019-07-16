# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # Iterate through marged_arr to insert smallest item in arrA and arrB until merged_arr is full
    for i in range(0, len(merged_arr)):
        # If arrA is empty, use arrB to fill
        if len(arrA) == 0:
            merged_arr[i] = min(arrB)
            arrB.remove(min(arrB))
        
        # If arrB is empty, use arrA to fill
        elif len(arrB) == 0:
            merged_arr[i] = min(arrA)
            arrA.remove(min(arrA))

        # If the smallest item in arrA is smaller than the smallest item in arrB, insert arrA's smallest item and then remove from arrA
        elif min(arrA) < min(arrB):
            merged_arr[i] = min(arrA)
            arrA.remove(min(arrA))

        # If the smallest item in arrB is smaller than the smallest item in arrA, insert arrB's smallest item and then remove from arrB
        elif min(arrA) >= min(arrB):
            merged_arr[i] = min(arrB)
            arrB.remove(min(arrB))
    
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr