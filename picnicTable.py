def printPicnic(itemDict, leftWidth, rightWidth):
    print('PICNIC ITEM'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
pinicItem = {'sandwich': 4, 'apple': 12, 'cups': 4, 'cookies': 8000}
printPicnic(pinicItem, 12, 5)
printPicnic(pinicItem, 20, 6)