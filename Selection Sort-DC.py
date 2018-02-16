a = [50,54,76,134,567,98,23]
b = [-9,98,65,-23,897,123,98]
def selection(lst):
    for i in range(0, len(lst)):
        mini = i
        for j in range(i+1, len(lst), +1):
            if(lst[j] < lst[mini]):
                mini = j
        temp = lst[i]
        lst[i] = lst[mini]
        lst[mini] = temp
    return(lst)

print(selection(a))
print(selection(b))
