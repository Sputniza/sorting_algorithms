# quick sort

def quicksort(items):
    
    # set pivot to mid for minimizing encounter of worst case in partly sorted lists
    
    if len(items) > 1:
        
        pivot_index = len(items)/2
        smaller_items = []
        larger_items = []
        
        for i, val in enumerate(items):
            
            if i != pivot_index:
            
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)
        
        quicksort(smaller_items)
        quicksort(larger_items)        
                                
        items[:] = smaller_items + [items[pivot_index]] + larger_items        
                
                

# merge sort

def mergesort(items):
 
    
    if len(items) > 1:    
    
        # split lists
        mid = len(items)/2
        
        left = items [0:mid]
        right = items [mid:]
        
        # sort parts of list in place
        mergesort(left)
        mergesort(right)
        
        # merging left and right list
        
        l, r = 0, 0
        for i in range(len(items)):
            
            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None
            
            if (lval is not None and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (rval is not None and lval >= rval) or lval is None:
                items[i] = rval
                r += 1
                
            else:
                raise Exception('Could not merge, sub arrays sizes do not match the main array')

                
                

# bubble sort

def bubblesort(items):
    # implementation of bubble sort
    
    for i in range(len(items)):
        for j in range(len(items)-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1],items[j]   # swap items
    return items


# insertion sort

def insertionsort(items):
    
    for i in range(1, len(items)):
        
        val = items[i]
        
        j = i
        while j > 0 and val < items[j-1]:
            # swap 
            items[j], items[j-1] = items[j-1], items[j] 
            j -= 1
