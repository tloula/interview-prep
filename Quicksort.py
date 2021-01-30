from random import randint

def quicksort(arr):
    if len(arr) < 2: return arr
    smaller, equal, larger = [], [], []
    pivot = arr[randint(0, len(arr)-1)]

    for x in arr:
        if x < pivot: smaller.append(x)
        elif x == pivot: equal.append(x)
        else: larger.append(x)

    return quicksort(smaller) + equal + quicksort(larger)

def quicksort_2(arr, lo, hi):
    if len(arr) < 2: return arr
    if lo < hi:
        pi = partition(arr, lo, hi)
        quicksort_2(arr, lo, pi-1)
        quicksort_2(arr, pi+1, hi)

def partition(arr, lo, hi):
    i = lo - 1
    pivot = arr[hi]
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1

arr = [1, 2, 7, 5, 6, 12, 5, 7, 32, 87, 1, 2, 5]

print(quicksort(arr))
print(quicksort_2(arr, 0, 12))
print(arr)