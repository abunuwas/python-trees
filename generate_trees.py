import random

def generateRawTree(numRows):
    tree = ''
    lengthTree = numRows
    for index in range(lengthTree):
        index += 1
        row = ''
        for i in range(index):
            i+=1
            newValue = random.randint(0, 50)
            row += str(newValue) + ' '
        tree += row.strip() + '\n' # the strip method is necessary to remove the trailing empty character that we used when declaring the variable row

    return tree

def rawTreeToFile(fileName, rawTree):
    tree = rawTree.splitlines()
    with open(fileName, 'w') as t:
        for line in tree:
            t.write(line)
            t.write('\n')

def getFromFile(file):
    rawTree = open(file, 'r', encoding='utf-8').read()
    return rawTree

def getTree(rawTree):
    rawTree = rawTree.splitlines()
    tree=[]
    for line in rawTree:
        tree.append([float(num) for num in line.split()])
    return tree

def generateTree(numRows, toFile='notToFile', fileName=None):
    rawTree = generateRawTree(numRows)
    if toFile == 'toFile':
        rawTreeToFile(fileName, rawTree)
        rawTree = getFromFile(fileName)
        tree = getTree(rawTree)
    elif toFile == 'notToFile':
        tree = getTree(rawTree)
    else: raise('Please provide a valid flag')
    return tree
    





