def shell (lst):
    n=len(lst)
    gap=n//2
    while gap>0 :
        #print(gap)
        for i in range (1, n):
            
            pos=i
            val=lst[i]
            if i>gap:
                while pos>0 and val<lst[pos-gap]:
                    lst[pos]=lst[pos-gap]
                    pos=pos-gap
                lst[pos]=val
            #print(lst)
        gap=gap//2
    print(lst)
a=[1,5,4,8,1,3,2,1]
shell(a)
                    
    
