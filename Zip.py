def Len(arg) :
    count = 0
    for i in arg:
        count += 1
    return count

def Range(start=0, end=0, step=1) :
    if start > end :
        start, end = end, start
    while start < end :
        yield start
        start += step

def All(args) :
    for i in Range(Len(args)) :
        if Len(args[i]) == Len(args[0]) :
            pass
        else :
            raise MemoryError("the amount is not the same")
    return True

def Zip(*args) :
    if All(args) :
        for i in Range(Len(args[0])) :
            List = []
            for j in Range(Len(args)) :
                List.append(args[j][i])
            yield List    

A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]
for x, y in Zip(A, B) :
    print(x, y)

