def bubblesort(list, noOfIter):
    iterNum = 0
# Swap the elements to arrange in order    for iter_num in range(len(list)-1,0,-1):
    for iter_num in range(noOfIter-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list           
'''
    while iterNum < noOfIter:
        for idx in range(iterNum):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
        iterNum += 1
    return list
'''
