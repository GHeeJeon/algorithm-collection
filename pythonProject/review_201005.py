"""
# 이진탐색트리
# 최악의 경우 효율이 안좋다.(N번 비교)
# 평균적으로 log(N)번 비교

# 삽입노드 ADL
def 삽입(a, val):
    if (a.root is None):
        a.setRoot(val)
    else:
        a.insertNode(a.root, val)


def 노드삽입(a, 현재노드, value):
    if (value <= 현재노드.value):
        if (현재노드.leftChild):
   /        else:
            현재노드.leftChild = Node(value)
    elif (value > 현재노드.value):
        if (현재노드.rightChild):
            a.insertNode(현재노드.rightChild, value)
        else:
            현재노드.rightChild = Node(value)
"""
