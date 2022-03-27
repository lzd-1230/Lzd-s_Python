"""
字典树和普通的数不同之处在于：其用边来保存字符信息，而不是用结点！
    但是存储空间浪费很多
"""
NUM_ALPHA=26
BASE_ASCII = 97

class Node():
    def __init__(self,type:int=0) -> None:
        self.type = type
        self.next = [None for i in range(NUM_ALPHA)]

# 字典树
class tri_tree():
    def __init__(self) -> None:
        num = int(input("需要插入几个单词"))
        self.root = Node()
        for i in range(num):
            tmp = input()
            self.insert(tmp) # 完成插入
        print("-------打印已添加的字典树---------")
        self.print_tree(self.root,0,[None for i in range(10)])
        tar = input("要查找的节点：")
        print(self.search_str(tar))

    def search_str(self,tar):
        tmp = self.root
        for ele in tar:
            code = self.map_alpha(ele)
            if(not tmp.next[code]): return False
            tmp = tmp.next[code]
        return True if tmp.type else False

    def map_alpha(self,tar):
        return ord(tar) - BASE_ASCII

    def insert(self,word):
        tmp = self.root
        for idx,alpha in enumerate(word):
            alpha_code = self.map_alpha(alpha)
            if(tmp.next[alpha_code] == None): 
                tmp.next[alpha_code] = Node() if idx != len(word)-1 else Node(1)
                tmp =  tmp.next[alpha_code]
            else:
                tmp = tmp.next[alpha_code]
        
    def get_node(self):
        return Node()        
    
    def list_tostr(self,a):
        b = [str(i) for i in a if i] # 如果i是None就不加入
        return "".join(b)

    # 用字典序打印所有单词(important)
    def print_tree(self,root,idx,buff):
        if(root == None): return
        if(root.type): 
            print(self.list_tostr(buff))
            return
        # 深度优先
        for i in range(NUM_ALPHA):
            buff[idx] = chr(i+BASE_ASCII)
            self.print_tree(root.next[i],idx+1,buff)
        return

if __name__ == "__main__":
    t = tri_tree()