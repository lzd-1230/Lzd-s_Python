"""
哈夫曼树的实现
"""
nodes = [("a",0.1),("b",0.2),("c",0.3),("d",0.15),("e",0.25)]





class Node(object):
    def __init__(self,ch,p,lchild=None,rchild=None) -> None:
        self.ch = ch
        self.p = p
        self.lchild=lchild
        self.rchild=rchild
        self.code = None

    def __repr__(self) -> str:
        return str((self.ch,self.p))

    def __lt__(self,other):
        return self.p < other.p # 越小越放在前面
    def __gt__(self,other):
        return self.p > other.p # 越小越放在前面

class HaffmanTree():
    def __init__(self) -> None:
        self.nodes = []
        self.codes = {}
    def get_encode(self,cur_node,cur_code):
        # 1.如果该节点是叶子节点
        if(not cur_node.lchild):
            self.codes[cur_node.ch]=cur_code
            return 1
        # 2.不是叶子节点
        cur_code+= "0"
        self.get_encode(cur_node.lchild,cur_code) # 递归左子树
        cur_code = cur_code[:-1]
        cur_code += "1"
        self.get_encode(cur_node.rchild,cur_code) # 递归右子树

    def init_tree(self,nodes_data):
        self.init_nodes(nodes_data)
        # 根据概率的排序来生成节点
        self.nodes.sort(reverse=True)
        for i in range(len(self.nodes)-1,0,-1): # [n-1,0]
            last1,last2 = self.nodes[i],self.nodes[i-1]
            new_node = self.merge_nodes(last1,last2)
            self.nodes.insert(i-1,new_node)
            new_idx = i-1
            # 安排新生成节点的位置
            for j in range(i-2,-1,-1):
                if(self.nodes[j] < self.nodes[new_idx]):
                    # 交换两个下标的值
                    self.nodes[new_idx],self.nodes[j] = self.nodes[j],self.nodes[new_idx]
                    new_idx -= 1
                else:
                    break
        # 拿到编码
        self.get_encode(self.nodes[0],"")
        return self.nodes[0]

    # 生成一个新的节点
    def merge_nodes(self,node1,node2):
        ch_new = node1.ch + node2.ch
        p_new = node1.p + node2.p
        new_node = self.get_node((ch_new,p_new),(node2,node1))
        return new_node

    def get_node(self,data,childs):
        return Node(*data,*childs)

    def init_nodes(self,datas):
        for data in datas:
            self.nodes.append(Node(*data))
        for data in datas:
            self.codes[data[0]]="" # 初始化编码字典
    def __str__(self) -> str:
        pass
if __name__ == "__main__":
    tree = HaffmanTree()
    root = tree.init_tree(nodes)
    print(tree.codes)