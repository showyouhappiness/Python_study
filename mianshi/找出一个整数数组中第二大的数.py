def find_second_largest(arr):
    if len(arr) < 2:
        return None

    first_max = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
        elif arr[i] > second_max and arr[i] != first_max:
            second_max = arr[i]

    return second_max


arr = [12, 5, 8, 12, 7]
second_largest = find_second_largest(arr)
print(second_largest)
