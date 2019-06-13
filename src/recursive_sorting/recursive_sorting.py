# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    arrA_index = 0
    arrB_index = 0

    for i in range(0, len(merged_arr)):
        while arrA_index < len(arrA) and arrB_index < len(arrB):

            if arrA[arrA_index] < arrB[arrB_index]:
                merged_arr[i] = arrA[arrA_index]
                arrA_index += 1
            
            else: 
                merged_arr[i] = arrB[arrB_index]
                arrB_index += 1
                
            i+=1
        
        if arrA_index < len(arrA):
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1

        if arrB_index < len(arrB):
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1

    return merged_arr

print(merge([2,5,6,9,13], [1,3,7,7,11,12,14]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
