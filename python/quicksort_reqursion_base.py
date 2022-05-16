# Should be optimized
def qsort(list):
    if list == []: 
        return []
    pivot = list[0]
    l = qsort([x for x in list[1:] if x < pivot])
    u = qsort([x for x in list[1:] if x >= pivot])
    return l + [pivot] + u
