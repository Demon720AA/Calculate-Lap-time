"""Qullify result"""
def check(nameList, timeList):
    '''check name'''
    nameCheck = nameList.count(nameList[-1])
    if nameCheck > 1:
        Location = nameList.index(nameList[-1])
        nameList.pop(-1)
        timeCheck = []
        timeCheck.append(timeList.pop(Location))
        timeCheck.append(timeList.pop(-1))
        timeCheck.sort()
        print(timeCheck)
        timeList.insert(Location, timeCheck[0])
        # time1 = timeList.pop(timeList[Location])
        # time2 = timeList.pop(timeList[-1])

def sort(nameList, timeList):
    '''sort'''
    check = timeList[0]
    search = 0
    sortName = []
    sortTime = []
    list1 = []
    for lenList in range(len(nameList), 0, -1):
        for count in range(lenList):
            if check > timeList[count]:
                check = timeList[count]
                # print(check)
            # print(timeList)
        # print(timeList)
        search = timeList.index(check)
        sortName.append(nameList.pop(search))
        sortTime.append(timeList.pop(search))
        if timeList != []:
            check = timeList[0]
    for _ in range(len(sortTime)):
        name = sortName.pop(0)
        time = sortTime.pop(0)
        n_t = name, time
        print(n_t)
        list1.append(n_t)
    return list1
