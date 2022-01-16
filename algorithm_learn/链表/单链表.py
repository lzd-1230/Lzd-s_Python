class Node():
    def __init__(self) -> None:
        self.next = None
        self.data = None

class Link_list():
    def __init__(self,length:int,datas:list) -> None:
        tmp = Node()
        self.phead = tmp # 指向头节点
        ptail = tmp
        for i in range(length):
            tmp = Node()
            # 节点赋初值
            ptail.next = tmp
            ptail = tmp 
            ptail.data = datas[i] 
    # 链表遍历
    def travel(self):
        ptmp = self.phead
        while(ptmp.next != None):
            print(ptmp.next.data)
            ptmp = ptmp.next
    # 链表反转
    def reverse(self):
        pre = None # 记录上一个操作的
        cur_node = self.phead.next # 首节点
        next_node = cur_node.next
        cur_node.next = None
        while(next_node != None):
            pre = cur_node
            cur_node = next_node
            next_node = cur_node.next
            cur_node.next = pre
        self.phead.next = cur_node
    # 删除给定值(如果是无头节点就复杂了,因此我们还是经常指定头节点)
    def remove_val(self,val):
        ptmp = self.phead.next # 从首节点开始检查
        pre_node = self.phead # 要执行了一次操作后才记录前一个节点
        while(ptmp!=None):
            if(ptmp.data == val):
                next_node = ptmp.next
                del ptmp # 删除这个节点
                pre_node.next = next_node
                ptmp = next_node
            else:
                pre_node = ptmp
                ptmp = ptmp.next
        
        
if __name__ == "__main__":
    init_data = ["d","a","a","b","c","a"] 
    Link = Link_list(5,init_data)
    # Link.reverse()
    Link.remove_val("a")
    Link.travel()


