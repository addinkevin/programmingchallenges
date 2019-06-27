"""
Trees: Is This a Binary Search Tree?

Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def _checkBSTAlt(root):
    """ Alternative version checking min and max in left and right tree """
    if not root: return False, None, None

    minLeft = maxLeft = None
    if root.left:
        isBSTLeft, minLeft, maxLeft = _checkBSTAlt(root.left)
        if not isBSTLeft or not (maxLeft < root.data):
            return False, None, None

    minRight = maxRight = None
    if root.right:
        isBSTRight, minRight, maxRight = _checkBSTAlt(root.right)
        if not isBSTRight or not (root.data < minRight):
            return False, None, None

    minValue = maxValue = root.data
    if minLeft:
        minValue = minLeft
    if maxRight:
        maxValue = maxRight

    return True, minValue, maxValue


def _preOrder(node, dataArray):
    if node.left:
        _preOrder(node.left, dataArray)

    dataArray.append(node.data)

    if node.right:
        _preOrder(node.right, dataArray)


def _checkBST(root):
    dataArray = []
    _preOrder(root, dataArray)

    for i in range(len(dataArray) - 1):
        if dataArray[i] >= dataArray[i + 1]:
            return False
    return True


def checkBST(root):
    if not root: return True
    return _checkBST(root)