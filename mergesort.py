import random, os

def mergesort(arr):

    if len(arr) > 1:

        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        mergesort(left_arr)
        mergesort(right_arr)

        left_el = 0
        right_el = 0
        arr_index = 0
        while left_el < len(left_arr) and right_el < len(right_arr):
            if left_arr[left_el] < right_arr[right_el]:
                arr[arr_index] = left_arr[left_el]
                left_el += 1

            else:
                arr[arr_index] = right_arr[right_el]
                right_el += 1

            arr_index += 1

        while left_el < len(left_arr):
            arr[arr_index] = left_arr[left_el]
            left_el += 1
            arr_index += 1

        while right_el < len(right_arr):
            arr[arr_index] = right_arr[right_el]
            right_el += 1
            arr_index += 1

array = [random.randint(0, 20) for i in range(5)]

os.system('cls')
print(array)
mergesort(array)
print(array)