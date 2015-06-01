print(range(16))
#grid = [0,4,0,0,0,4,4,4,2,2,4,2,2,2,2,8]

grid = [0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(grid)
upOppo = 4
downOppo = -4
leftOppo = 1
rightOppo = -1


def gridNav(startNum, dir):
    '''
    Returns a list of the column or row it is working on.

    Input: *Initial value to start traversing (int)
    *The dir you want it to go.
    Output: A list of that column or row (list of int) *(should only be four values, only)*

    '''
    if dir == -4:
        initialValueFixer = {0: 12, 1: 13, 2: 14, 3: 15, 12: 12, 13: 13, 14: 14, 15: 15}
        iterNum = initialValueFixer[startNum]
    elif dir == -1:
        initialValueFixer = {0: 3, 4: 7, 8: 11, 12: 15, 3: 3, 7: 7, 11: 11, 15: 15}
        iterNum = initialValueFixer[startNum]
    else:
        iterNum = startNum
    returnList = []
    if dir not in [-4, -1, 1, 4]:  # weeds out bad dir argument
        raise Exception("Please given me a dir of -4, -1, 1, or 4.")
    while iterNum < 16 and iterNum > 0:
        returnList.append(grid[iterNum])
        iterNum = iterNum + dir
    if len(returnList) < 2:
        raise Exception("The program started with the wrong initialValue.")
    return returnList


def isSame(fourItemList, startNum=0):
    '''
    Returns true if an index of the fourItemList is equal to another index down the list.

    Input: *fourItemList ~ The result of gridNav() - basically a four item list (int list)
        *startNum ~ The index at which to eval the likeness of two numbers. 0 is default (int 0 through 3)
    Output: True or False - Did a number match somewhere down the list.

    '''
    print str(fourItemList) + 'this'
    i = startNum
    while i < 3:  # ensures the index, i, doesn't grab an index of fourItemList that doesn't exist.
        if fourItemList[startNum] == fourItemList[i + 1] and fourItemList[i+1] != 0:
            return (True,  i+1)  # the adjacent does match the fourItemList[startNum] therefore sameness!
        i = i + 1
        print i
    return (False, 0)  # adjacent doens't match, then no sameness.


def transfromBlocks(fourItemList, dir):

    newFourItemList = fourItemList
    i = 0
    while i < 4:
        isSameTuple = isSame(fourItemList, i)
        if isSameTuple[0] is True:
            newFourItemList[i] = fourItemList[i]*2
            newFourItemList[isSameTuple[1]] = 0
        i = i + 1
    #push together terms
    i = 0
    listOfZerosToDel = []
    while i < 3:
        if newFourItemList[i] == 0:
            listOfZerosToDel.append(i)
        i = i + 1
    print listOfZerosToDel
    i = 0
    while i < len(listOfZerosToDel):
        newFourItemList.pop(listOfZerosToDel[i]-i)
        i += 1
    for y in range(len(listOfZerosToDel)):
        newFourItemList.append(0)
    return newFourItemList


def stitching(grid, dir):

    i = 0
    returnList = [[], [], [], []]
    # orderOfLists = {4: [0, 1, 2, 3], -4: [12, 13, 14, 15], 1: [0, 4, 8, 12], -1: [3, 7, 11, 15]}
    while i < 4:  # 4 number of columns or rows
        #orderOfLists[dir][i]
        returnList[0] = gridNav(i, dir)


def hello():
    pass

# print(gridNav(1,-4))
# print(isSame(gridNav(13,-4),0))

# print(transfromBlocks(gridNav(1,-4),4))
print(stitching[0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
