# Swap function 
def swap_positions(l, pos1, pos2): 
    l[pos1], l[pos2] = l[pos2], l[pos1] 
    return l
