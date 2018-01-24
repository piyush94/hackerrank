# code
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def create_tree(root, n):
    print(n)
    root = Tree()
    root.right = Tree()
    root.left = Tree()
    if n > 0:
        create_tree(root.right, n - 1)
        create_tree(root.left, n - 1)
    return root


def create_list(tempList, count):
    outList = []
    for i in range(count):
        outList.append(tempList[i] + tempList[i + 1])
    outList.reverse()
    return outList


def mainFN():
    T = int(input())
    for i in range(T):
        n = int(input())
        inputList = list(map(int, input().split()))
        for j in range(n - 1):
            tempList = create_list(inputList, n - j - 1)
            for k in tempList:
                inputList.insert(0, k)
        print(*inputList)


mainFN()
