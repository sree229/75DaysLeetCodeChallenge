class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None
class MyLinkedList(object):
    def __init__(self):
        self.head = None 

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        ptr = self.head
        count = 0
        while ptr!=None and count<index:
            ptr = ptr.next
            count+=1 
        return ptr.val if ptr else -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        temp  = Node(val)
        temp.next = self.head
        self.head = temp


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        temp  = Node(val)
        if self.head == None :
            self.head = temp 
            return 
        ptr = self.head
        while ptr.next !=None:
            ptr = ptr.next
        ptr.next = temp

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """ 
        temp  = Node(val)
        if index<=0:
            self.addAtHead(val)
            return 
        ptr = self.head
        count = 0
        while ptr!=None and count < index-1:
            ptr = ptr.next
            count +=1
        if ptr is None:
            return
        temp.next = ptr.next
        ptr.next = temp

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index<0 or self.head == None :
            return
        if index == 0:
            self.head = self.head.next
            return
        ptr = self.head
        count = 0
        while ptr!=None and count<index-1:
            ptr = ptr.next
            count+=1 
        if ptr is None or ptr.next is None:
            return 
        ptr.next = ptr.next.next
    

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)