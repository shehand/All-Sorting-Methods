def bb_sort(alist):
    n =  len(alist)-1
    for i in range(0,n):
        for j in range(n,i,-1):
            if alist[j-1] > alist[j]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp
    return l 
    
            
    
l = [8,6,2,1,3,8,65,5,68,89,8,5]
bb_sort(l)
