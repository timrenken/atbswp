tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

colWidth = [0] * len(tableData)

for x in range(len(tableData)):
    for y in range(len(tableData[x])):
        width = int(len(tableData[x][y]))
        if width > colWidth[x]:
            colWidth[x] = width

def printTable():
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(colWidth[x]),end=' ')
        print()

printTable()        




