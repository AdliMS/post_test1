import random, os
 
# fungsi quicksort
def sort(arr, low_index, high_index):
    
    if (low_index < high_index):

        partition_pos = partition(arr, low_index, high_index) # untuk menentukan posisi partisi
        sort(arr, low_index, partition_pos - 1) # quicksort untuk bagian yang lebih kecil dari pivot
        sort(arr, partition_pos + 1, high_index) # quicksort untuk bagian yang lebih besar dari pivot

def partition(arr, low_index, high_index):

    left = low_index
    right = high_index - 1
    pivot_index = random.randint(low_index, high_index)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high_index] = arr[high_index], arr[pivot_index]

    while left < right:

        while arr[left] < pivot and left < high_index:
            left += 1

        while arr[right] > pivot and right > low_index:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left] 

    if arr[left] > pivot:
        arr[left], arr[high_index] = arr[high_index], arr[left]

    return left

def quicksort(arr):
    sort(arr, 0, len(arr) - 1)

os.system('cls')

array = [random.randint(0, 20) for i in range(7)]

print(array)
quicksort(array)
print(array)