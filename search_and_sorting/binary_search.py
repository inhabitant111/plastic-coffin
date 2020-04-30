def binary_search(data, x):
    if data == sorted(data):
        first = 0
        last = len(data) - 1
        while first <= last:
            mid = (first + last) // 2
            if x == data[mid]:
                return mid
            elif x > data[mid]:
                first = mid + 1
            else:
                last = mid - 1
        return None
    else:
        print("List must be sorted!")