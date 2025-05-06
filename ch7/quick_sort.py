import random

def quick_sort(arr):
    # 피벗을 뽑는다.

    # 왼쪽 배열에 피벗보다 작은 값을 담는다.
    # 오른쪽 배열에 피벗보다 큰 값을 담는다.
    # 왼쪽 배열을 대상으로 퀵소트를 재수행한다.
    # 왼쪽 배열과 오른쪽 배열을 결합한다.

    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = []
    greater = []
    equal = []

    for item in arr:
        if item > pivot :
            greater.append(item)
        elif item < pivot :
            less.append(item)
        else :
            equal.append(item)

    # less, equal, greater
    return quick_sort(less) + equal + quick_sort(greater)

arr1 = [6, 1, 9, 3, 7, 2, 8, 4, 5]
arr2 = [3, 7, 2, 8, 1, 5, 9, 4, 6]
arr3 = [9, 4, 2, 7, 1, 8, 5, 6, 3]

print(quick_sort(arr1))
print(quick_sort(arr2))
print(quick_sort(arr3))