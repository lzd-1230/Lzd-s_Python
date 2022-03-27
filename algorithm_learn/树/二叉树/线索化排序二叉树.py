"""
不能用递归去遍历二叉树,因为堆栈和高度成正比
因此不用递归去实现遍历是很必要
自己画一颗二叉树感受一下
"""
import random

class Node():
    def __init__(self,val,lchild=None,rchild=None,ltag=False,rtag=False) -> None:
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
        self.ltag = ltag
        self.rtag=rtag

class Sort_Tree():
    pre = None
    def __init__(self) -> None:
        self.root = None

    def __get_node(self,val=None):
        return Node(val) 

    def insert_node(self,cur_node,val=None):
        if(cur_node == None): 
            return self.__get_node(val)
        if(cur_node.val == val): 
            return cur_node
        if(cur_node.val < val):
            cur_node.rchild = self.insert_node(cur_node.rchild,val)
            return cur_node
        else:
            cur_node.lchild = self.insert_node(cur_node.lchild,val)
            return cur_node # 这里一定要返回一个东西,否则上层调用就会被置为None
        
    def travel_origin(self,cur_node):
        if(cur_node == None):
            return
        if(not cur_node.ltag):
            self.travel_origin(cur_node.lchild)
        print(cur_node.val,end=" ")
        self.travel_origin(cur_node.rchild)

    def build_index(self,cur_node):
        if(cur_node == None):
            return
        self.build_index(cur_node.lchild) # 这里直接到达最左边的节点
        # 前驱和后继的设置
        if(not cur_node.lchild):
            cur_node.lchild = self.pre
            cur_node.ltag = True
        if(self.pre != None and self.pre.rchild == None):
            self.pre.rchild = cur_node
            self.pre.rtag = True
        # 左边已经弄完了
        self.pre = cur_node
        # 弄右边
        self.build_index(cur_node.rchild)
        return

    def __leftmost(self,cur_node):
        p = cur_node
        # 先走到最开头
        while(p and p.ltag==False and p.lchild):
            p = p.lchild
        return p
    def travel_index(self,cur_node):
        p = self.__leftmost(cur_node)
        # 开始向后遍历
        while(p):
            print(p.val,end = " ")
            if(p.rtag == False):
                p = p.rchild
            else:
                p = self.__leftmost(p.rchild)

              

if __name__ == "__main__":
    test = [1,2,3,4]
    t = Sort_Tree()
    t.root = t.insert_node(t.root,0)
    for ele in test:
        t.insert_node(t.root,ele)
    print("传统中序遍历")
    t.travel_origin(t.root)
    print("")
    # 建立线索化
    t.build_index(t.root)
    t.travel_index(t.root)

