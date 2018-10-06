

def permutate(arr):
    print arr
    arr.sort()
    print arr
    temp = [0] * len(arr)
    turn = False
    c1 = 0
    c2 = 1
    for i in arr:
        if turn:
            temp[c1] = i
            turn = False
            c1+=1
        else:
            temp[-c2] = i
            turn = True
            c2+=1
    return temp
def make_1000(arr):
    for i in arr:
        if i > .75* max(arr):
            arr.pop(i)
            arr.append(1000)
        return arr

print (make_1000([1,2,3,4,5,7,5,8]))
