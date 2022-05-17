def quick(sequence):
    
    if len(sequence) <= 1:
        return sequence
    else:
        pivot_point = sequence[len(sequence) // 2]
        sequence.remove(pivot_point)
    
    less = quick([i for i in sequence if i < pivot_point])
    more = quick([j for j in sequence if j >= pivot_point])
    
    return less + [pivot_point] + more
    

print(quick([4, 3, 2, 2, 1, 6, 5, 5, 5]))
