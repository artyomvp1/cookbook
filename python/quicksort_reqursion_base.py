# Option 2
def quick1(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot_point = sequence[len(sequence) // 2]    # pivot point in the middle
    
    less = []
    more = []
    
    for i in sequence:
        if i > pivot_point:
            more.append(i)
        elif i == pivot_point:    # iteration should not go over pivot point
            continue
        else:
            less.append(i)
    
    return quick1(less) + [pivot_point] + quick1(more)


print(quick1([7, 5, 6, 3, 4, 1, 2]))


# The most delicate
def quick(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence[len(sequence) // 2]
    
    more = quick([i for i in sequence if i > pivot if i != pivot])
    less = quick([j for j in sequence if j <= pivot if j != pivot])
    
    return less + [pivot] + more


print(quick([5, 3, 4, 2, 1]))
