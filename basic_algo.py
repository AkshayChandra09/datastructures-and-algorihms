def binary_search(array, target):
    if len(array) == 0:
        return None
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None


def first_and_last_index(arr, number):
    index = binary_search(arr, number)
    if index is None:
        return None
    if arr[index - 1] != number and arr[index + 1] != number:
        return index
    else:
        left = index - 1
        right = index + 1
        while left > 0 and right < len(arr) - 1 and arr[left] == number and arr[right] == number:
            if arr[left] == number:
                left -= 1
            if arr[right] == number:
                right += 1
        return [left, right]


arr = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6]
number = first_and_last_index(arr, 2)
print(number)

