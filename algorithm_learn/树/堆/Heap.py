

class Min_Heap():
    def __init__(self,size=10) -> None:
        self.cnt = 0
        self.size = size
        self.data = [None for i in range(size+1)]
    def get_top(self):
        return self.data[1]

    def is_empty(self):
        return self.cnt == 0


    def is_full(self):
        return self.cnt == self.size

    def push(self,ele):
        if(self.is_full()):
            return None
        self.cnt += 1
        self.data[self.cnt] = ele 
        idx = self.cnt
        # 调整位置
        while(idx>>1 and self.data[idx]<self.data[idx>>1]):
            self.data[idx],self.data[idx>>1] = self.data[idx>>1], self.data[idx]
            idx = idx>>1
        return True

    def pop(self):
        if(self.is_empty()):
            return None
        pop_data = self.data[1]
        self.data[1] = self.data[self.cnt]
        self.cnt -= 1
        idx = 1
    
        while(idx<<1 <= self.cnt):
            tmp = idx
            # 找出左右孩子中最小的那一个
            left ,right = idx <<1 ,idx <<1 | 1
            if(self.data[idx] > self.data[left]): tmp = left
            if(right<=self.cnt and self.data[tmp] > self.data[right]): tmp = right
            if(tmp == idx): break  # 没变就不用调整了
            self.data[tmp],self.data[idx] = self.data[idx],self.data[tmp]
        return pop_data

if __name__ == "__main__":
    heap = Min_Heap()
    for i in range(10,0,-1):
        heap.push(i)
    print(heap.get_top())
    print(heap.data)
    print(heap.is_full())
