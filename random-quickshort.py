import random as rand

def quicksort(arr, first, last):
    if (first < last):

        pivotidx = random_partition(arr, first, last)
        quicksort(arr, first, pivotidx - 1)
        quicksort(arr, pivotidx + 1, last)

def random_partition(arr, first, last):
    random_pivot = rand.randrange(first, last)

    arr[first], arr[random_pivot] = arr[random_pivot], arr[first]

    return partition(arr, first, last)

def partition(arr, first, last):
    pivot = first
    i = first + 1

    for j in range(first + 1, last + 1):

        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return(pivot)

array=[6,8,4,8,2,3,5,10]
quicksort(array, 0, len(array)-1)
print(array)
