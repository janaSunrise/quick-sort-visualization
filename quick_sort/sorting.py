def quicksort(array: list) -> list:
    array = array.copy()
    left, equal, right = [], [], []

    if len(array) < 2:
        return array

    pivot = array[0]
    for x in array:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            right.append(x)

    return quicksort(left) + equal + quicksort(right)
