def stalin_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        if len(sorted_arr) == 0 or arr[i] >= sorted_arr[-1]:
            sorted_arr.append(arr[i])
    return sorted_arr


