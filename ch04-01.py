class Node():
    def __init__(self):
        self.data = None
        self.link = None

# 첫번째 노드 생성 - 링크 필요 x
node1 = Node()
node1.data = "다현0"
# 두 번째 노드 생성 - 첫 번쨰 노드와 연결
node2 = Node()
node2.data = "다현1"
node1.next = node2

node3 = Node()
node3.data = "다현2"
node2.next = node3

node4 = Node()
node4.data = "다현3"
node3.next = node4

node5 = Node()
node5.data = "다현4"
node4.next = node5

print(node1.data)
print(node1.lnk.data, end=" ")
print(node1.lnk.link.data, end=" ")
print(node1.lnk.link.link.data, end=" ")
print(node1.lnk.link.link.link.data, end=" ")
















