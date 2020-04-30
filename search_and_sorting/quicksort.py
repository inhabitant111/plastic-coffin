def quicksort(data):
    import random
    if len(data) <= 1:
        return data
    else:
        pivot = random.choice(data)
        less = [i for i in data if i < pivot]
        equal = [pivot] * data.count(pivot)
        greater = [i for i in data if i > pivot]
        return quicksort(less) + equal + quicksort(greater)