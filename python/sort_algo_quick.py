def quick(sequence):
    
    if len(sequence) <= 1:
        return sequence
    
    pivot_point = sequence[0]
    
    less = [i for i in sequence if i < pivot_point]
    more = [j for j in sequence if j > pivot_point]
    midd = [k for k in sequence if k == pivot_point]
    
    return quick(less) + midd + quick(more)
                                     
